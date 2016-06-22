#coding: utf-8
from django.shortcuts import render 
from django.http import HttpResponseRedirect, HttpResponse
from .models import WorkType, Journal 
from django.contrib.auth.decorators import login_required  
from .forms import JournalForm 
from django.forms import formset_factory
from django.db import IntegrityError, transaction 
from django.contrib import messages

@login_required
def create(request):
    #user = request.user
    JournalFormSet = formset_factory(JournalForm, max_num=0)

    # Get our existing data for this user.  This is used as initial data.
    data = Journal.objects.all()
    current_data = [{
        'count_all': l.count_all, 
        'count_current': l.count_current, 
        'val_all': l.val_all, 
        'val_current': l.val_current, 
        'position': l.position, 
        'work_type_id': l.work_type_id, 
        'work_type_pos_smeta': l.work_type.pos_smeta, 
        'work_type_num_unit': l.work_type.num_unit, 
        'work_type_unit': l.work_type.unit, 
        'work_type_price_unit': l.work_type.price_unit,
        'work_type_name': l.work_type.name
        } for l in data]

    if request.method == 'POST':
        data_formset = JournalFormSet(request.POST)

        if data_formset.is_valid():
            # Now save the data for each form in the formset
            new_data = []

            for data_form in data_formset:
                count_all = data_form.cleaned_data.get('count_all')
                count_current = data_form.cleaned_data.get('count_current')
                val_all = data_form.cleaned_data.get('val_all')
                val_current = data_form.cleaned_data.get('val_current') 
                position = data_form.cleaned_data.get('position') 
                work_type_id = data_form.cleaned_data.get('work_type_id')

                new_data.append(Journal(
                    count_all=count_all, 
                    count_current=count_current, 
                    val_all=val_all, 
                    val_current=val_current, 
                    position=position, 
                    work_type_id=work_type_id
                    ))

            try:
                with transaction.atomic():
                    #Replace the old with the new
                    Journal.objects.all().delete()
                    Journal.objects.bulk_create(new_data)

                    # And notify our users that it worked
                    messages.success(request, 'Данные обновлены!')
                    return HttpResponseRedirect('http://127.0.0.1:8000/oad/create/')

            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error saving your profile.')
                #return redirect(reverse('profile-settings'))

    else:
        data_formset = JournalFormSet(initial=current_data)

    context = {
        'data_formset': data_formset,
    }

    return render(request, 'oad/create2.html', context)