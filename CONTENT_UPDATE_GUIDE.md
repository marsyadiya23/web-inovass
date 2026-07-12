# 📝 Content Update Guide

## How to Add Content to Detail Pages

All 44 detail pages currently show "Coming Soon" placeholders. When you're ready to add actual content, follow this guide.

## 📋 Option 1: Use the Full Content Template

The page `layanan-detail-penyusunan-dokumen.html` has complete content. Use it as a reference template.

### Sections in Full Template:
1. **Hero Section** - Large image background with title
2. **Features Grid** - 4 cards highlighting key benefits
3. **Key Features** - Image + bullet point list
4. **Scope Section** - Numbered cards showing service scope
5. **Benefits Section** - Text + image layout
6. **Outputs Section** - What clients receive
7. **CTA Section** - Final call-to-action
8. **Footer** - Standard footer

### To Clone This Structure:
```bash
# Copy the full template
cp layanan-detail-penyusunan-dokumen.html layanan-detail-YOUR-SERVICE.html

# Edit the new file:
# 1. Update title in <title> tag
# 2. Update breadcrumb navigation
# 3. Replace all content sections
# 4. Update image paths if needed
```

## 📋 Option 2: Keep Simple Structure, Add Content Sections

You can keep the current clean design and add content between the header and coming soon sections.

### Step-by-Step:

1. **Open the detail page** you want to edit
2. **Find this comment** in the HTML:
   ```html
   <!-- COMING SOON PLACEHOLDER -->
   ```
3. **Add your content BEFORE this section**

### Example Content Section:

```html
<!-- YOUR CONTENT HERE -->
<section style="padding: 4rem 2rem; background: white;">
  <div style="max-width: 1200px; margin: 0 auto;">
    
    <h2 style="font-size: 2rem; color: #1e3a8a; margin-bottom: 1.5rem;">
      Deskripsi Layanan
    </h2>
    
    <p style="font-size: 1.1rem; color: #6b7280; line-height: 1.8; margin-bottom: 2rem;">
      Tambahkan deskripsi lengkap layanan Anda di sini...
    </p>

    <h3 style="font-size: 1.5rem; color: #1a1a1a; margin-bottom: 1rem;">
      Manfaat
    </h3>
    
    <ul style="list-style: none; padding: 0;">
      <li style="padding: 0.5rem 0; color: #374151;">
        ✅ Manfaat pertama
      </li>
      <li style="padding: 0.5rem 0; color: #374151;">
        ✅ Manfaat kedua
      </li>
      <li style="padding: 0.5rem 0; color: #374151;">
        ✅ Manfaat ketiga
      </li>
    </ul>

  </div>
</section>
```

4. **Remove or keep the "Coming Soon" section** depending on your needs
   - Keep it if content is still partial
   - Remove it if content is complete

## 🎨 Pre-Built Content Components

Use these CSS classes from `pages.css` for consistent styling:

### Feature Cards Grid:
```html
<section class="detail-features">
  <div class="detail-features-container">
    
    <div class="detail-feature-card">
      <div class="detail-feature-icon">
        <!-- SVG icon here -->
      </div>
      <h3>Feature Title</h3>
      <p>Feature description text</p>
    </div>
    
    <!-- Repeat for more cards -->
    
  </div>
</section>
```

### Key Features (Image + Text):
```html
<section class="detail-key-features">
  <div class="detail-key-container">
    <div class="detail-key-image">
      <img src="image/your-image.png" alt="Description" />
    </div>
    <div class="detail-key-content">
      <h2>Section Title</h2>
      <ul class="detail-key-list">
        <li>Point 1</li>
        <li>Point 2</li>
        <li>Point 3</li>
      </ul>
    </div>
  </div>
</section>
```

### Scope Section (Numbered Cards):
```html
<section class="detail-scope">
  <div class="detail-scope-container">
    <h2 class="detail-section-title">Ruang Lingkup</h2>
    <p class="detail-section-subtitle">Subtitle text</p>
    
    <div class="detail-scope-grid">
      
      <div class="detail-scope-card">
        <div class="detail-scope-number">01</div>
        <h3>Item Title</h3>
        <ul>
          <li>Point 1</li>
          <li>Point 2</li>
        </ul>
      </div>
      
      <!-- Repeat for more items -->
      
    </div>
  </div>
</section>
```

### Benefits Section:
```html
<section class="detail-benefits">
  <div class="detail-benefits-container">
    <div class="detail-benefits-content">
      <h2>Benefits Title</h2>
      <ul class="detail-benefits-list">
        <li>
          <strong>Benefit Title</strong>
          <p>Benefit description</p>
        </li>
      </ul>
    </div>
    <div class="detail-benefits-image">
      <img src="image/your-image.png" alt="Description" />
    </div>
  </div>
</section>
```

## 🔄 Option 3: Automated Batch Updates

If you need to update multiple pages at once:

### Create a Python Script:

```python
#!/usr/bin/env python3
"""Add content to specific detail pages"""

# Define pages and their content
pages_content = {
    'layanan-detail-jasa-sertifikasi-iso.html': {
        'description': 'Your service description here...',
        'benefits': ['Benefit 1', 'Benefit 2', 'Benefit 3'],
    },
    # Add more pages...
}

# Read, modify, write each file
for filename, content in pages_content.items():
    with open(filename, 'r') as f:
        html = f.read()
    
    # Insert content before "COMING SOON" section
    new_section = f'''
    <!-- SERVICE CONTENT -->
    <section style="padding: 4rem 2rem; background: white;">
      <div style="max-width: 1200px; margin: 0 auto;">
        <h2>Deskripsi</h2>
        <p>{content['description']}</p>
      </div>
    </section>
    '''
    
    html = html.replace('<!-- COMING SOON PLACEHOLDER -->', 
                       new_section + '\n  <!-- COMING SOON PLACEHOLDER -->')
    
    with open(filename, 'w') as f:
        f.write(html)
    
    print(f'✅ Updated: {filename}')
```

## 🖼️ Images

### Where to Place Images:
```
web_inovass/
└── image/
    ├── layanan kami.jpeg (already exists)
    ├── image1.png (already exists)
    ├── image2.png (already exists)
    ├── your-new-image-1.jpg
    └── your-new-image-2.png
```

### How to Reference:
```html
<img src="image/your-new-image-1.jpg" alt="Descriptive text" />
```

### Image Recommendations:
- **Hero images**: 1920x600px, landscape
- **Feature images**: 800x600px, landscape
- **Icon images**: 400x400px, square
- **Format**: JPEG for photos, PNG for graphics
- **Size**: < 500KB per image

## 📱 Responsive Testing

After adding content, test on:
- ✅ Desktop (1920px, 1440px, 1024px)
- ✅ Tablet (768px, 1024px)
- ✅ Mobile (375px, 414px, 390px)

### Quick Test Commands:
```bash
# Open in browser
open layanan-detail-YOUR-SERVICE.html

# Or use browser DevTools:
# 1. Right-click → Inspect
# 2. Click device toolbar icon
# 3. Test different screen sizes
```

## 🎨 Color Reference

When adding custom content, use these colors:

```css
/* Primary */
Navy:   #1e3a8a   /* Headings, important elements */
Green:  #00c278   /* CTAs, accents, success */

/* Text */
Dark:   #1a1a1a   /* Main headings */
Body:   #374151   /* Body text */
Light:  #6b7280   /* Secondary text */

/* Backgrounds */
White:  #ffffff   /* Cards, sections */
Gray:   #f8f9fa   /* Alternate sections */
```

## ✅ Content Checklist

Before publishing a page with new content:

- [ ] All images load correctly
- [ ] All links work (no 404s)
- [ ] Text is readable and properly formatted
- [ ] Mobile layout looks good
- [ ] Breadcrumb navigation updated
- [ ] Page title updated
- [ ] Meta description updated (if SEO matters)
- [ ] No console errors
- [ ] Smooth scrolling
- [ ] CTAs point to correct pages

## 🚀 Quick Tips

### DO:
✅ Keep sections consistent across pages  
✅ Use the provided CSS classes  
✅ Test on mobile devices  
✅ Optimize images before uploading  
✅ Use descriptive alt text  
✅ Keep content concise and scannable  

### DON'T:
❌ Add inline styles if a CSS class exists  
❌ Use very large images (>1MB)  
❌ Forget to update breadcrumb  
❌ Mix different design patterns  
❌ Skip mobile testing  
❌ Use tiny fonts (<14px on mobile)  

## 📞 Need Help?

If you get stuck:
1. Check `layanan-detail-penyusunan-dokumen.html` for reference
2. Review `pages.css` for available styles
3. Test one page first before batch updates
4. Keep backups of working versions

---

**Last Updated:** July 12, 2026  
**Template Version:** 2.0  
**Status:** Ready for content
