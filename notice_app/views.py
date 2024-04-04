from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Board
from .forms import AddBoardForm

def home_page(requeset):
    boards = Board.objects.all().order_by('-posted_date')[:8]
    context = {
        'boards': boards
    }

    return render(requeset, "./home_page.html", context)

# CREATE
def add_board_page(request):
    if request.method == "POST":
        form = AddBoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AddBoardForm()

    context = {
        'form': form
    }

    return render(request, "./add_board_page.html", context)

# VIEW
def board_detail_page(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board
    }
    return render(request, "./board_detail_page.html", context)

# DELETE
def delete_board_page(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect("home_page")

    context = {
        'board': board
    }

    return render(request, "./delete_board_page.html", context)

# UPDATE
def edit_board_page(request, pk):
    board = get_object_or_404(Board, pk=pk)
    form = AddBoardForm(request.POST or None, request.FILES or None, instance=board)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("board_detail_page", pk=board.pk)

    context = {
        'board': board,
        'form': form
    }

    return render(request, "./edit_board_page.html", context)
