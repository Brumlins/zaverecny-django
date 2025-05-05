from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

def members(request):
    all_members = Member.objects.all().order_by('-joined_date')

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members')
    else:
        form = MemberForm()

    return render(request, 'members/members.html', {
        'members': all_members,
        'form': form
    })

def add_member(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST.get('email')
        joined_date = request.POST.get('joined_date')
        Member.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            joined_date=joined_date or None
        )
    return redirect('members')

def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('members')
    return render(request, 'members/confirm_delete.html', {'member': member})



def edit_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.firstname = request.POST['firstname']
        member.lastname = request.POST['lastname']
        member.email = request.POST.get('email')
        member.joined_date = request.POST.get('joined_date') or None
        member.save()
        return redirect('members')
    return render(request, 'members/edit_member.html', {'member': member})


def recepty(request):
    context = {
        'title' : 'Recepty'

    }
    title = 'Recepty'
    return render(request, 'index.html', context=context)
