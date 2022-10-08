from django.shortcuts import render,redirect
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

def all_todos(request):
	all_data = ToDOWorks.objects.all()
	return render(request,'todo_list.html',{'all_data':all_data})


def add_todos(request):
	all_data = ToDOWorks.objects.all()
	if request.method =="POST":
		name = request.POST.get('worktodo')
		data = ToDOWorks(name_of_work=name)
		data.save()
		return redirect('/')
	return render(request,'todo_list.html',{'all_data':all_data})


def todo_delete(request,id):
	data = ToDOWorks.objects.get(id=id)
	data.delete()
	return redirect('/')



# here is api based crude operctions 

class todoapiview(APIView):
	def get(self,request):
		all_data = ToDOWorks.objects.all()
		serilizer = todoSerializer(all_data,many=True)
		return Response(serilizer.data)
	def post(self,request):
		serilizer = todoSerializer(data=request.data)
		if serilizer.is_valid():
			serilizer.save()
			return Response(serilizer.data)

class handlecrud(APIView):
	def get_object(self, pk):
		try:
			return ToDOWorks.objects.get(pk=pk)
		except ToDOWorks.DoesNotExist:
			raise Http404
	def get(self, request, pk, format=None):
	    todo = self.get_object(pk)
	    serializer = todoSerializer(todo)
	    return Response(serializer.data)
	def put(self, request, pk, format=None):
	    todo = self.get_object(pk)
	    serializer = todoSerializer(todo, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
	    todo = self.get_object(pk)
	    todo.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)
