"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os


[(dir+1)%2 and os.rename(f'target/{dir}', f'target/hack{dir}') for dir in map(int, os.listdir('target'))]
