import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan fungsi matematis
def f_linear(x):
    return 2 * x + 1        # f(x) = 2x + 1

def f_kuadrat(x):
    return x ** 2 - 3 * x  # f(x) = x² - 3x

def f_kubik(x):
    return x ** 3 - x      # f(x) = x³ - x

# Membuat data
x = np.linspace(-4, 4, 200)

# Visualisasi
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(x, f_linear(x), color='royalblue', linewidth=2)
axes[0].set_title('f(x) = 2x + 1 (Linear)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].axhline(0, color='gray', linewidth=0.8)
axes[0].axvline(0, color='gray', linewidth=0.8)
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, f_kuadrat(x), color='tomato', linewidth=2)
axes[1].set_title('f(x) = x² − 3x (Kuadrat)')
axes[1].set_xlabel('x')
axes[1].axhline(0, color='gray', linewidth=0.8)
axes[1].axvline(0, color='gray', linewidth=0.8)
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, f_kubik(x), color='seagreen', linewidth=2)
axes[2].set_title('f(x) = x³ − x (Kubik)')
axes[2].set_xlabel('x')
axes[2].axhline(0, color='gray', linewidth=0.8)
axes[2].axvline(0, color='gray', linewidth=0.8)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('grafik_fungsi.png', dpi=150)
plt.show()
print("Grafik disimpan sebagai grafik_fungsi.png")