from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import urlencode

from .models import DataRecord


SORT_OPTIONS = {
    'recent': ('Сначала новые', '-created_at'),
    'oldest': ('Сначала старые', 'created_at'),
    'title': ('По названию', 'title'),
    'category': ('По категории', 'category'),
    'status': ('По статусу', 'status'),
    'priority': ('По приоритету', 'priority'),
}


def _filtered_records(request):
    records = DataRecord.objects.all()
    search = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()
    status = request.GET.get('status', '').strip()
    priority = request.GET.get('priority', '').strip()
    sort = request.GET.get('sort', 'recent')

    if search:
        records = records.filter(title__icontains=search) | records.filter(
            category__icontains=search
        ) | records.filter(status__icontains=search) | records.filter(
            description__icontains=search
        )
    if category:
        records = records.filter(category__icontains=category)
    if status:
        records = records.filter(status__icontains=status)
    if priority:
        records = records.filter(priority=priority)

    sort_field = SORT_OPTIONS.get(sort, SORT_OPTIONS['recent'])[1]
    return records.order_by(sort_field, 'title'), sort


def record_list(request):
    records, selected_sort = _filtered_records(request)
    context = {
        'records': records,
        'priority_choices': DataRecord.Priority.choices,
        'sort_options': SORT_OPTIONS,
        'selected_sort': selected_sort,
        'query': request.GET,
    }
    return render(request, 'yadro/home.html', context)


def add_record(request):
    if request.method == 'POST':
        DataRecord.objects.create(
            title=request.POST.get('title', '').strip(),
            category=request.POST.get('category', '').strip(),
            status=request.POST.get('status', '').strip(),
            priority=request.POST.get('priority') or DataRecord.Priority.MEDIUM,
            description=request.POST.get('description', '').strip(),
        )
    return redirect('yadro:record_list')


def update_record(request, pk):
    record = get_object_or_404(DataRecord, pk=pk)
    if request.method == 'POST':
        record.title = request.POST.get('title', record.title).strip()
        record.category = request.POST.get('category', record.category).strip()
        record.status = request.POST.get('status', record.status).strip()
        record.priority = request.POST.get('priority') or record.priority
        record.description = request.POST.get('description', record.description).strip()
        record.is_active = request.POST.get('is_active') == 'on'
        record.save()
    redirect_url = reverse('yadro:record_list')
    if request.GET:
        redirect_url = f'{redirect_url}?{urlencode(request.GET)}'
    return redirect(redirect_url)


def delete_record(request, pk):
    record = get_object_or_404(DataRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
    return redirect('yadro:record_list')
