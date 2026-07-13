from django.shortcuts import render, redirect
from django.utils import timezone
from .models import DailyTask, FlexTask

def dashboard(request):
    today = timezone.now().date()
    
    # 1. Auto-seed core tasks if empty
    if not DailyTask.objects.filter(date=today).exists():
        for name in ["Finance 1", "Finance 2", "Finance 3", "Finance 4", "Build 1", "Build 2"]:
            DailyTask.objects.create(task_name=name, date=today)
    
    # 2. Handle POST (Save + Add)
    if request.method == "POST":
        # Save edited names and checkboxes
        for key, value in request.POST.items():
            if key.startswith("name_core_"):
                t_id = key.split("_")[2]
                task = DailyTask.objects.get(id=t_id)
                task.task_name = value
                task.is_complete = f"check_core_{t_id}" in request.POST
                task.save()
            elif key.startswith("name_flex_"):
                t_id = key.split("_")[2]
                task = FlexTask.objects.get(id=t_id)
                task.task_name = value
                task.is_complete = f"check_flex_{t_id}" in request.POST
                task.save()
        
        # Add new item
        if "add_task" in request.POST and request.POST.get("new_task"):
            if FlexTask.objects.filter(date=today).count() < 4:
                FlexTask.objects.create(task_name=request.POST["new_task"], date=today)
        
        return redirect('dashboard')

    # 3. Calculations
    core = DailyTask.objects.filter(date=today)
    flex = FlexTask.objects.filter(date=today)
    total_credits = sum(t.credit_value for t in core if t.is_complete) + \
                    sum(t.credit_value for t in flex if t.is_complete)
    
    return render(request, 'dashboard.html', {
        'core_tasks': core, 'flex_tasks': flex,
        'total_credits': total_credits,
        'hilton_fund': min(total_credits, 6000),
        'coaching_fund': max(0, total_credits - 6000)
    })