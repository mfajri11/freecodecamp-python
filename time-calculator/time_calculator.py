def add_time(start, duration, days=None):
  waktu, meridem = start.split()
  jam, menit = map(int, waktu.split(':'))
  jam_dur, menit_dur = map(int, duration.split(':'))
  hari = {
    'sunday' : 0,
    'monday' : 1,
    'tuesday' : 2,
    'wednesday': 3,
    'thrusday': 4,
    'friday': 5,
    'saturday':6
  }
  haris = list(hari.keys())
  n, index_hari = 0, ''
  # cek pm atau am
  if meridem == 'PM':
      jam += 12

  # 1 itung menit dulu
  # cek mereka nambah ke jam atau ngga
  next_jam = (menit + menit_dur) // 60
  # bikin menit jadi format 60 menit
  menit = (menit + menit_dur) % 60
  del menit_dur

  # 2 itung jam
  # cek ada tambahan dari jumlah menit atau ngga
  jam = (
    (jam + next_jam )
    if next_jam
    else jam
  )

  # cek harinya bakal nambah ngga diliat dari penjumlahan jam
  next_hari =  (jam + jam_dur) // 24
  # itung jam terus bikin format 24 jam
  jam = (jam + jam_dur) % 24
  del jam_dur
  if days:
      ihari = hari[days.lower()]
      ihari = (
        (ihari + next_hari ) % 7
        if next_hari
        else ihari)
      days = haris[ihari].capitalize()
  if next_hari == 1:
      n = 1
      index_hari = ' (next day)'
  elif next_hari > 1:
      n = next_hari
      index_hari = f' ({n} days later)'


  # ubah ke pm atau am
  if jam == 0:
      jam = 12
      meridem = 'AM'
  elif jam - 12 > 0 and menit:
      jam = jam-12
      meridem = 'PM'
  elif jam == 12:
    meridem = 'PM'
  else:
      meridem = 'AM'

  # bikin format printnya
  if menit < 10:
      menit = '0' + str(menit)
  waktu = f'{jam}:{menit} {meridem}' 
  new_time = f'{waktu}, {days}{index_hari}' if days else f'{waktu}{index_hari}'
  return new_time