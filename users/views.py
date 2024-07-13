from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import *
from django.contrib.auth import logout, authenticate, login
from .serializers import UserSerializers, RegisterSerializer


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs, 'name': request.user.username}
    return render(request, 'home.html', context)


def login_view(request):
    return render(request, 'login.html')


@login_required
def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)


@login_required
def see_blog(request):
    blog_list = BlogModel.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(blog_list, 10)  # Show 10 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'see_blog.html', {'blog_objs': page_obj})



@login_required
def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
        
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)


def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug=slug)

        # Check if the current user is the author of the blog post
        if blog_obj.user != request.user:
            return redirect('/')

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog_obj)
            if form.is_valid():
                form.save()  # This will update the existing blog_obj
                return redirect('/')  # Redirect to home or some other page after successful update
        else:
            # Populate the form with initial data from existing blog_obj
            form = BlogForm(instance=blog_obj)

        context['blog_obj'] = blog_obj
        context['form'] = form
    except BlogModel.DoesNotExist:
        # Handle the case where the blog with given slug does not exist
        return redirect('/')  # Redirect to home or some other page

    return render(request, 'update_blog.html', context)


# def blog_update(request, slug):
#     context = {}
#     try:
#
#         blog_obj = BlogModel.objects.get(slug=slug)
#
#         if blog_obj.user != request.user:
#             return redirect('/')
#
#         initial_dict = {'content': blog_obj.content}
#         form = BlogForm(initial=initial_dict)
#         if request.method == 'POST':
#             form = BlogForm(request.POST)
#             image = request.FILES['image']
#             title = request.POST.get('title')
#             user = request.user
#
#             if form.is_valid():
#                 content = form.cleaned_data['content']
#
#                 blog_obj = BlogModel.objects.create(
#                     user=user, title=title,
#                     content=content, image=image
#                 )
#                 print(blog_obj)
#
#         context['blog_obj'] = blog_obj
#         context['form'] = form
#     except Exception as e:
#         print(e)
#
#     return render(request, 'update_blog.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/see-blog/')


def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token)

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e:
        print(e)

    return redirect('/')


# class RegisterApi(APIView):
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializers(user, context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })