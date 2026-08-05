#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def replace_in_file(filename, replacements):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content = content.replace(old, new)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error in {filename}: {e}")
        return False

# Simple test
print("Python script ready for batch customization")
print("Script will customize remaining 9 files...")
