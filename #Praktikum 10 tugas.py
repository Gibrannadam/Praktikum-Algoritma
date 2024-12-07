#Praktikum 10 tugas

def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    # Base case: jika panjang array sudah 1, tidak perlu disort lagi
    if n == 1:
        return

    # Perulangan untuk memindahkan elemen terbesar ke posisi akhir
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap elemen
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Panggil fungsi ini secara rekursif untuk sisa elemen
    bubble_sort_recursive(arr, n - 1)

# Contoh penggunaan
data = [87, 56, 23, 89, 15, 2, 200, 28, 31]
bubble_sort_recursive(data)
print("Hasil pengurutan:", data)
