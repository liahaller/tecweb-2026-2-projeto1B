from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag', '').strip()
        if tag_name:
            tag, created = Tag.objects.get_or_create(name=tag_name)
        else:
            tag = None
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title=title, content=content, tag=tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, note_id):
    note = Note.objects.get(id=note_id) #busca a nota pelo id
    note.delete() #apaga a note
    return redirect('index') #volta pra pg inicial

def update(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        tag_name = request.POST.get('tag', '').strip()
        if tag_name:
            tag, created = Tag.objects.get_or_create(name=tag_name)
        else:
            tag = None
        note.tag = tag
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})

def tag_list(request):
    all_tags = Tag.objects.order_by('name')
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})






