/* Pencarian Layanan: kotak cari di bawah tab kategori, mencari di SEMUA halaman layanan
   (indeks assets/data/layanan.json, dibangun CI oleh scripts/build-layanan-index.py).
   Dipasang di 7 halaman layanan/<kategori>/index.html. Tautan bisa dibagikan: ?q=iso+9001 */
(function () {
  var root = new URL('../../', document.currentScript.src);
  var anchor = document.getElementById('navTabsSection');
  var content = document.querySelector('.service-content-section');
  if (!anchor || !content) return;

  var css = document.createElement('style');
  css.textContent =
    '.lsr{max-width:1200px;margin:1.5rem auto 0;padding:0 1.5rem}' +
    '.lsr-box{position:relative}' +
    '.lsr-box svg{position:absolute;left:1.1rem;top:50%;width:20px;height:20px;transform:translateY(-50%);color:#6b8f80;pointer-events:none}' +
    '.lsr input{width:100%;box-sizing:border-box;font:inherit;font-size:1rem;padding:.95rem 1.2rem .95rem 3rem;border:1.5px solid #d6e2dc;border-radius:999px;background:#fff;color:#0a1628;outline:none;transition:border-color .2s,box-shadow .2s}' +
    '.lsr input:focus{border-color:#00c278;box-shadow:0 0 0 4px rgba(0,194,120,.15)}' +
    '.lsr-meta{margin:.8rem .4rem 0;font-size:.85rem;color:#6b8f80}' +
    '.lsr-list{list-style:none;margin:1rem 0 3rem;padding:0;display:grid;gap:.6rem}' +
    '.lsr-list a{display:block;padding:1rem 1.2rem;border:1px solid #e3ebe7;border-radius:14px;background:#fff;text-decoration:none;transition:border-color .2s,box-shadow .2s}' +
    '.lsr-list a:hover,.lsr-list a:focus{border-color:#00c278;box-shadow:0 6px 20px rgba(3,13,20,.06)}' +
    '.lsr-t{display:block;font-weight:600;color:#0a1628;line-height:1.4}' +
    '.lsr-c{display:block;margin-top:.25rem;font-size:.82rem;color:#6b8f80}' +
    '.lsr-list mark{background:#d9f7ea;color:inherit;border-radius:3px;padding:0 1px}' +
    '.lsr-empty{padding:1.5rem 1.2rem;border:1px dashed #d6e2dc;border-radius:14px;color:#334155;margin:1rem 0 3rem}' +
    '.lsr-empty a{color:#00a066;font-weight:600}';
  document.head.appendChild(css);

  var wrap = document.createElement('div');
  wrap.className = 'lsr';
  wrap.innerHTML =
    '<label class="lsr-box"><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Cari layanan</span>' +
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>' +
    '<input type="search" autocomplete="off" placeholder="Cari layanan, mis. ISO 9001, audit internal, 17025, kalibrasi…" /></label>' +
    '<p class="lsr-meta" aria-live="polite"></p><div class="lsr-out"></div>';
  anchor.insertAdjacentElement('afterend', wrap);

  var input = wrap.querySelector('input');
  var meta = wrap.querySelector('.lsr-meta');
  var out = wrap.querySelector('.lsr-out');
  var data = null;

  // huruf kecil, tanpa aksen, tanda baca jadi spasi: "ISO/IEC 17025:2017" → "iso iec 17025 2017"
  function norm(s) {
    return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  }
  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function mark(s, words) {
    var re = new RegExp('\\b(' + words.map(function (w) { return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')', 'gi');
    return esc(s).replace(re, '<mark>$1</mark>');
  }

  function render() {
    var q = norm(input.value);
    var url = new URL(location.href);
    q ? url.searchParams.set('q', input.value.trim()) : url.searchParams.delete('q');
    history.replaceState(null, '', url);

    if (!q) { out.innerHTML = ''; meta.textContent = ''; content.style.display = ""; return; }
    content.style.display = "none";
    if (!data) { meta.textContent = 'Memuat…'; return; }

    var words = q.split(' ');
    // cocok di AWAL kata: "9001" menemukan ISO 9001 tetapi bukan ISO 39001; "kalib" tetap menemukan "kalibrasi"
    var hits = data.filter(function (d) { return words.every(function (w) { return d.h.indexOf(' ' + w) !== -1; }); });
    // judul yang memuat seluruh frasa tampil lebih dulu
    hits.sort(function (a, b) { return (b.n.indexOf(' ' + q) !== -1) - (a.n.indexOf(' ' + q) !== -1); });

    if (!hits.length) {
      meta.textContent = '';
      out.innerHTML = '<div class="lsr-empty">Tidak ada layanan yang cocok dengan “' + esc(input.value.trim()) +
        '”. Coba kata lain, atau <a href="' + root + 'kontak.html">hubungi kami</a> untuk kebutuhan khusus.</div>';
      return;
    }
    var shown = hits.slice(0, 60);
    meta.textContent = hits.length + ' layanan ditemukan' + (hits.length > shown.length ? ' (60 teratas ditampilkan, perjelas kata kunci)' : '');
    out.innerHTML = '<ul class="lsr-list">' + shown.map(function (d) {
      return '<li><a href="' + root + d.u + '"><span class="lsr-t">' + mark(d.t, words) + '</span><span class="lsr-c">' +
        esc(d.c) + (d.p ? ' › ' + esc(d.p) : '') + '</span></a></li>';
    }).join('') + '</ul>';
  }

  var timer;
  input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(render, 120); });
  input.addEventListener('keydown', function (e) { if (e.key === 'Escape') { input.value = ''; render(); } });

  fetch(new URL('assets/data/layanan.json', root))
    .then(function (r) { return r.json(); })
    .then(function (items) {
      data = items.map(function (d) { d.n = ' ' + norm(d.t); d.h = ' ' + norm(d.t + ' ' + d.c + ' ' + (d.p || '')); return d; });
      render();
    })
    .catch(function () { meta.textContent = 'Pencarian sedang tidak tersedia.'; });

  var initial = new URLSearchParams(location.search).get('q');
  if (initial) { input.value = initial; render(); }
})();
