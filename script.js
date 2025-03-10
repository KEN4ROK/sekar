// Ambil elemen tombol dan pesan rahasia
const tombolLucu = document.getElementById('tombol-lucu');
const pesanRahasia = document.getElementById('pesan-rahasia');

// Tambahkan event listener untuk tombol
tombolLucu.addEventListener('click', function() {
  // Tampilkan pesan rahasia
  pesanRahasia.classList.remove('hidden');

  // Animasi kecil
  tombolLucu.textContent = 'Yey! 🎊';
  tombolLucu.style.backgroundColor = '#ff1493';
});