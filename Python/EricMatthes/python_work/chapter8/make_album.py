def make_album(name_signer, name_album, count_row = ''):
    list = {'signer':name_signer, 'album':name_album}
    if count_row:
	    list['count_row'] = count_row
    return list
while True:
    print("\nOur programm start")
    print("(enter 'q' for finish programm)")
    n_signer = input("Enter name signer: ")
    
    if n_signer == 'q':
	    break
    n_album = input("Enter name album: ")
    if n_album == 'q':
	    break
    c_row = input("Enter count row: ")
    album = make_album(n_signer, n_album, c_row)
    print(album)