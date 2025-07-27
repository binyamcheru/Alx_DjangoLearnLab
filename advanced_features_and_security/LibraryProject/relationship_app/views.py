from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  #اسم التمبليت المستخدم
    context_object_name = 'library_info'                     #اسم المتغير المستخدم في التمبليت


'''<!-- library_detail.html -->
<h1>{{ library_info.name }}</h1>
<ul>
  {% for book in library_info.books.all %}
    <li>{{ book.title }}</li>
  {% endfor %}
</ul>
'''
#_____________
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):            #function-based view to sign-up/register
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ← ده السطر اللي بيدور عليه
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

#عشان نقدر نكتب في القالب مثلًا: {{ form }} أو {{ form.username }} وغيره.
#username is attritbtute in UserCreationForm class >>> username, password1 and password2 are attribtutes in UserCreationForm class

#_________________________
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role     #is user in userprofile class 
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
     return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


#____________________
#✅ إنشاء ملف forms.py في مجلد relationship_app/
#افتح مجلد relationship_app، واعمل ملف جديد اسمه forms.py، وداخل الملف ده حط الكود التالي:


#from django import forms
#from .models import Book

#class BookForm(forms.ModelForm):
#    class Meta:
#        model = Book
#        fields = ['title', 'author']

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # يجب أن تكون عامل فورم مسبقًا للـ Book

@permission_required('relationship_app.can_add_book', raise_exception=True) #in models.py
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
   
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)  #in models.py
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST': # المستخدم بعت بيانات من فورم
        form = BookForm(request.POST, instance=book)  #استقبل البيانات اللي المستخدم كتبها (request.POST) #اربطها مع الكتاب الحالي (instance=book) → عشان يتم تعديل نفس الكائن، مش إنشاء كائن جديد.
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else: # غالبًا المستخدم بس فتح الصفحة
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/book_form.html', {'form': form})  #send key 'form' which has value form to page: book_form.html

@permission_required('relationship_app.can_delete_book', raise_exception=True)  #in models.py
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

#_________________
