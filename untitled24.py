# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fsHuPqs8zVdND28iPibO9rfZSeaz4Y0I
"""

import numpy as np
import matplotlib.pyplot as plt

# Ma'lumotlar
x = np.linspace(0, 10, 100)  # 0 dan 10 gacha 100 ta nuqta
y = np.sin(x)  # Sinus qiymatlari

# Grafikni chizish
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sinus(x)', color='blue')  # Grafik chizish
plt.title('Sinus Funksiyasining Grafikı')  # Sarlavha
plt.xlabel('X qiymatlari')  # X o'qi
plt.ylabel('Y qiymatlari')  # Y o'qi
plt.grid(True)  # To'r
plt.legend()  # Afsonani qo'shish
plt.show()  # Grafikni ko'rsatish

import numpy as np
import matplotlib.pyplot as plt

# Tasodifiy ma'lumotlar yaratish
np.random.seed(0)  # Natijalarni takrorlanadigan qilish uchun
x = np.random.uniform(0, 10, 50)  # 0 dan 10 gacha 50 ta tasodifiy X qiymatlar
y = np.random.uniform(0, 10, 50)  # 0 dan 10 gacha 50 ta tasodifiy Y qiymatlar

# Scatter grafik chizish
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Nuqtalar', alpha=0.8)  # Tasodifiy nuqtalar
plt.title('Tasodifiy Nuqtalar Scatter Grafiki')  # Sarlavha
plt.xlabel('X qiymatlari')  # X o'qi
plt.ylabel('Y qiymatlari')  # Y o'qi
plt.grid(True)  # To'r
plt.legend()  # Afsonani qo'shish
plt.show()  # Grafikni ko'rsatish