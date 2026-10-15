def steplfsr(lfsr):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr

ct_hex = "30cbb50e507774fdafd01e0bfdbc38d5eadf92991cdd347064e37444e517d661cea9"
ct_bytes = bytes.fromhex(ct_hex)

for seed_awal in range(256):
    lfsr = seed_awal
    hasil_dekripsi = bytearray()
    
    for c in ct_bytes:
        lfsr = steplfsr(lfsr)
        ks = lfsr
        hasil_dekripsi.append(c ^ ks)
    
    if hasil_dekripsi.startswith(b"academy{"):
        print("Seed awal LFSR ", seed_awal)
        print(hasil_dekripsi.decode())
        break