from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesListView(ListView, LoginRequiredMixin):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    # use the user data in the request to query all the data
    def get_queryset(self):
        return self.request.user.notes.all()


def notes(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes_list.html',{'notes':all_notes})

# Look at the ListView and DetailView
class NoteItemView(DetailView, LoginRequiredMixin):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'

def note_item(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/note_detail.html', {'note':note})

class NoteCreateView(CreateView, LoginRequiredMixin):
    """
    This is the most abstracted view function I have seen, I think the CreateView meta type has done lots of
    background work.
    Class-based view in Django is really a powerful dark magic, it contains so much powerful functionalities
    """
    model = Note
    form_class = NoteForm
    success_url = '/notes'
    template_name = 'notes/create_note_form.html'

    def form_valid(self, form):
        # Make sure the form data is saved into an object but does not save/commit to the db directly
        self.object = form.save(commit=False)
        # Bundle the note with the user instance, which will be stored as the foreign key
        self.object.user = self.request.user
        # Save the note object into the db
        self.object.save()
        # redirect into the success_url
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(UpdateView, LoginRequiredMixin):
    model = Note
    form_class = NoteForm
    success_url = '/notes'
    template_name = 'notes/create_note_form.html'


class NoteDeleteView(DeleteView, LoginRequiredMixin):
    model = Note
    success_url = '/notes'
    template_name = 'notes/note_delete.html'