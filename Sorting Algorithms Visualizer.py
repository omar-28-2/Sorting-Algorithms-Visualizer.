from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
import time
import random
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Sorting Visualizer Application")
root.maxsize(1400, 800)
root.config(bg = "#219ebc")
root.resizable(True,True)

Algorithms_type = StringVar()
list_Algorithms = ['Bubble Sort', 'Cocktail Shaker Sort', 'Cycle Sort', 'Gnome Sort', 'Heap Sort', 'Insertion Sort', 'Merge Sort', 'Odd Even Sort', 'Quick Sort', 'Selection Sort']

speed_type = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

arr = []
sort_arr=[]

def displayArr(arr, colorArray):
    canvas.delete("all")
    canvas_width = 1000
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i,h in enumerate(tempArr):
        x1 = i * width_x + ini + space
        y1 = canvas_height - h * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])
        canvas.create_text(x1 + 2, y1, anchor=SW, text=str(arr[i]))
    root.update()


def createArray():
    global arr

    array_size = 20
    range_begin = 0
    range_end = 100

    arr = []
    for m in range(0,array_size ):  
        random_integer = random.randint(range_begin, range_end) #starting from a higher value and not 0 because the vertical bars wont be visible
        arr.append(random_integer)
        #sort_arr= sorted(arr)
    displayArr(arr, ["#003049" for x in range(len(arr))])

    
def process_input():
    global arr
    user_input = entry.get()
    try :
        array = [int(x) for x in user_input.split(",")]
        arr = []
        for i in array:
            arr.append(i)
            displayArr(arr, ['#003049' for i in range(len(arr))])
            entry.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input: please enter numbers separated by commas")
        entry.delete(0, END)

def speed():

    slow = 0.8
    medium = 0.5
    fast = 0.00001

    if speed_comboBox.get() == 'Slow':
        return slow
    elif speed_comboBox.get() == 'Medium':
        return medium
    elif speed_comboBox.get() =="Fast":
        return fast

#Quick Sort

def partition(arr, start, end, displayArr, tym ):
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            displayArr(arr, ["#264653" if x == low or x == high else "#023047" for x in range(len(arr))])
            time.sleep(tym)
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    displayArr(arr, ["#003049" if x == start or x == high else "#003049" for x in range(len(arr))])
    time.sleep(tym)

    return high

def quick_sort(arr, start, end, displayArr, tym):
    if start >= end:
        return

    p = partition(arr, start, end,displayArr,tym)
    quick_sort(arr, start, p-1, displayArr, tym)
    quick_sort(arr, p+1, end, displayArr, tym)

#Heap Sort

def Heap(arr, n, i, displayArr, tym):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        displayArr(arr, ["#264653" if x == i or x == largest else "#023047" for x in range(len(arr))])
        time.sleep(tym)
        Heap(arr, n, largest, displayArr, tym)

def HeapSort(arr, displayArr, tym):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        Heap(arr, n, i, displayArr, tym)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        displayArr(arr, ["#264653" if x == i or x == 0 else "#023047" for x in range(len(arr))])
        time.sleep(tym)
        Heap(arr, i, 0, displayArr, tym)

#Merge sort
def merge(arr, start, mid, end, displayArr):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(arr[q])
            q+=1
        elif q > end:
            tempArray.append(arr[p])
            p+=1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p+=1
        else:
            tempArray.append(arr[q])
            q+=1

    for p in range(len(tempArray)):
        arr[start] = tempArray[p]
        start += 1

def merge_sort(arr, start, end, displayArr, tym):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(arr, start, mid, displayArr, tym)
        merge_sort(arr, mid+1, end, displayArr, tym)

        merge(arr, start, mid, end, displayArr)

        displayArr(arr, ["#264653" if x >= start and x < mid else "#023047" if x == mid 
                        else "#264653" if x > mid and x <=end else "#023047" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["#003049" for x in range(len(arr))])

#Gnome Sort
def GnomeSort(arr, displayArr, tym):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            displayArr(arr, ["#264653" if x == index or x == index - 1 else "#023047" for x in range(len(arr))])
            time.sleep(tym)
            index -= 1

#Odd Even Sort
def OddEvenSort(arr, displayArr, tym):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayArr(arr, ["#264653" if x == i or x == i + 1 else "#023047" for x in range(len(arr))])
                time.sleep(tym)
                sorted = False
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayArr(arr, ["#264653" if x == i or x == i+1 else "#023047" for x in range(len(arr))])
                time.sleep(tym)
                sorted = False

#Cocktail Shaker Sort

def CocktailShaker(arr, displayArr, tym):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while(swapped == True):
        swapped = False
        for i in range(start, end):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayArr(arr, ['#264653' if x == i or x == i+1 else "#023047" for x in range(len(arr))])
                time.sleep(tym)
                swapped = True
        if(swapped == False):
            break
        swapped = False
        end = end - 1 #backward pass
        for i in range(end-1, start-1, -1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayArr(arr, ["#264653" if x == i or x == i + 1 else "#023047" for x in range(len(arr))])
                time.sleep(tym)
                swapped = True
        start = start + 1

#Cycle Sort
def CycleSort(arr, displayArr, tym):
    n = len(arr)
    for cycleStart in range(0, n-1):
        item = arr[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        displayArr(arr, ["#264653" if x == pos or x == cycleStart else "#023047" for x in range(len(arr))])
        time.sleep(tym)
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            displayArr(arr, ["#264653" if x == pos or x == cycleStart else "#023047" for x in range(len(arr))])
            time.sleep(tym)


def sort():
    
    if sorted(arr) == arr:
        messagebox.showinfo("Already Sorted", "The array is already sorted.")
        return

    tym = speed()
    n = len(arr)

    if comboBox.get()=='Merge Sort':
        merge_sort(arr, 0, len(arr)-1, displayArr, tym)
        messagebox.showinfo("The sorrted arr", sorted(arr))    

    elif comboBox.get()=='Selection Sort':
        for i in range(0,n-1):
            for j in range(i+1,n):
                if (arr[i]>arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]  

                    displayArr(arr, ["#264653" if x == j or x == j+1 else "#023047" for x in range(len(arr))])
                    time.sleep(tym)
                        
        displayArr(arr, ["#003049" for x in range(len(arr))])
        messagebox.showinfo("The sorrted arr", sorted(arr))

    elif comboBox.get()=='Bubble Sort':
        for i in range(n-1):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                    displayArr(arr, ["#264653" if x == j else "#023047" if x==j+1 else "#2a9d8f" for x in range(len(arr))])
                    time.sleep(tym)
        messagebox.showinfo("The sorrted arr", sorted(arr))
        displayArr(arr, ["#003049" for x in range(len(arr))])

    elif comboBox.get()=='Insertion Sort':
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while (j >=0 and key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
                displayArr(arr, ["#264653" if x == j else "#023047" if x==j+1 else "#2a9d8f" for x in range(len(arr))])
                time.sleep(tym)
            arr[j+1] = key
        messagebox.showinfo("The Sorrted Array", sorted(arr))
        displayArr(arr, ["#87CEFA" for x in range(len(arr))])

    elif comboBox.get()=='Quick Sort':
        quick_sort(arr,0,len(arr)-1,displayArr, tym)
        messagebox.showinfo("The Sorrted Array", sorted(arr))

    elif comboBox.get() == 'Heap Sort':
        HeapSort(arr, displayArr, tym)
        messagebox.showinfo("The Sorted Array", sorted(arr))

    elif comboBox.get() == 'Gnome Sort':
        GnomeSort(arr, displayArr, tym)
        messagebox.showinfo("The Sorted Array", sorted(arr))

    elif comboBox.get() == 'Odd Even Sort':
        OddEvenSort(arr, displayArr, tym)
        messagebox.showinfo("The Sorted Array", sorted(arr))

    elif comboBox.get() == 'Cocktail Shaker Sort':
        CocktailShaker(arr, displayArr, tym)
        messagebox.showinfo("The Sorted Array", sorted(arr))

    elif comboBox.get() == 'Cycle Sort':
        CycleSort(arr, displayArr, tym)
        messagebox.showinfo("The Sorted Array", sorted(arr))

def resetArray():
    global arr
    arr = []
    displayArr(arr, [])

window = Frame(root, width= 1000, height=500, bg="#219ebc")
window.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(window, text="Sorting Type", bg="#219ebc" , font = ('tajawal' , 12 , 'bold'))
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

comboBox = ttk.Combobox(window, textvariable=Algorithms_type, values=list_Algorithms)
comboBox.grid(row=0, column=1, padx=5, pady=5)
comboBox.current(0)

lbl2 = Label(window, text="Speed", bg="#219ebc", font=('tajawal', 13, 'bold'))
lbl2.place(x=10, y=44)

speed_comboBox = ttk.Combobox(window, textvariable=speed_type, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

b1 = Button(window, text="Sort", command=sort, bg="#8ecae6" ,  width=15 , font = ('tajawal' , 12 , 'bold'))
b1.grid(row=10, column=15, padx=5, pady=5)

b2 = Button(window, text="Create Array", command=createArray, bg="#8ecae6", width=15 , font = ('tajawal' , 12 , 'bold'))
b2.grid(row=0, column=3, padx=5, pady=5)

b3 = Button(window, text="Reset Graph", command=resetArray, bg="#8ecae6", width=15 , font = ('tajawal' , 12 , 'bold'))
b3.place(x=420, y=43)

canvas = Canvas(root, width=1000, height=1000, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

quit_button = Button(root, text="close", command=root.destroy, width=15 , height="1", font = ('tajawal' , 12 , 'bold'), bg="#8ecae6" )
quit_button.place(x=725, y=45)  

Label(window, text="Enter numbers sperate by (,)", bg='#219ebc', font=(('tajawal' , 12 , 'bold'))).grid(row=10, column=0, padx=5, pady=5 )
entry = Entry(window, width=25)
entry.grid(row=10, column=1, padx=15, pady=10)
Button(window, text="Enter Input", height=1, width=15, fg='black', bg='#8ecae6', font = ('tajawal' , 12 , 'bold'), command=process_input).grid(row=10, column=3, padx=5, pady=5)



root.mainloop()