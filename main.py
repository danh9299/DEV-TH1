#hàm đọc dữ liệu tài khoản trong file
def READ_DATA_ACCOUNT(data_account):
	data_file = open('data_account.txt','r')
	read_data = data_file.readlines()
	if (read_data == []):
		data_file.close()
		return
	else:
		for i in read_data:
			data = i.split()
			data_account[data[0]] = data[1]
		data_file.close()
#hàm kiểm tra đăng nhập
def LOGIN(data_account):
	while 1:
		tai_khoan = input('Tài khoản : ')
		mat_khau = input('Mật khẩu : ')
		if (tai_khoan in data_account) and (data_account[tai_khoan] == mat_khau):
			print('Đăng nhập thành công.')
			return True
		elif (tai_khoan == '') or (mat_khau == ''):
			print('Bạn chưa điền thông tin đăng nhập !')
		else:
			print('Thông tin tài khoản hoặc mật khẩu chưa chính xác !')
		select = input('Bạn có muốn thử lại không ? (Y/N) : ')
		if (select == 'N' or select == 'n'):
			print('\n')
			return False
#hàm dành cho người quản trị
def ACCOUNT_MANAGE(data_account):
	#hàm ghi tài khoản đăng ký vào 1 file
	def WRITE_DATA_ACCOUNT(data_account):
		write_data = open('data_account.txt','w')
		for i in data_account.items():
			write_data.writelines([i[0],' ',i[1],'\n'])
		write_data.close()
	#hàm đăng ký tài khoản mới
	def REGISTER(data_account):
		while 1:
			tai_khoan_moi = input('Tài khoản mới : ')
			mat_khau_moi = input('Mật khẩu : ')
			if (tai_khoan_moi not in data_account):
				print('Đăng ký tài khoản thành công.')
				data_account [tai_khoan_moi] = mat_khau_moi
				WRITE_DATA_ACCOUNT(data_account)
			else:
				print('Tài khoản đã tồn tại !\n')
			select = input('Bạn có muốn tạo thêm tài khoản không ? (Y/N) : ')
			if (select == 'N' or select == 'n'):
				print('\n')
				return
	#hàm xóa tài khoản
	def DELETE_ACCOUNT(data_account):
		del_account = input('Nhập tài khoản cần xóa : ')
		if (del_account in data_account):
			select = input(f'Bạn có chắc chắn muốn xóa tài khoản "{del_account}" không ? (Y/N) : ')
			if (select == 'Y' or select == 'y'):
				del data_account[del_account]
				WRITE_DATA_ACCOUNT(data_account)
				print('Xóa tài khoản thành công.')
				return
			else:
				print('\n')
				return
		else:
			print('Tài khoản không tồn tại !')
			return
	#hàm in danh sách tài khoản
	def PRINT_DATA_ACCOUNT(data_account):
		for i in data_account.items():
			print(f'tài khoản : "{i[0]}" - mật khẩu : "{i[1]}"')
	while 1:
		print('\n\t\t---MENU MANAGE---')
		print('\t\t1. đăng ký')
		print('\t\t2. xóa tài khoản')
		print('\t\t3. hiển thị danh sách tài khoản')
		print('\t\t4. quay lại')
		n = input('nhập lựa chọn : ')
		if (n=='1'):
			REGISTER(data_account)
		elif (n=='2'):
			DELETE_ACCOUNT(data_account)
		elif (n=='3'):
			print('\n---DANH SÁCH TÀI KHOẢN VÀ MẬT KHẨU---')
			PRINT_DATA_ACCOUNT(data_account)
		elif (n=='4'):
			print('\n')
			return

#hàm đăng nhập chạy đầu tiên của chương trình
def BEGIN():
	data_account = dict()
	READ_DATA_ACCOUNT(data_account)
	while 1:
		print('\t\t---MENU LOGIN---')
		print('\t\t1. đăng nhập')
		print('\t\t2. quản lý tài khoản')
		print('\t\t3. thoát chương trình')
		n = input('nhập lựa chọn : ')
		if (n=='1'):
			if LOGIN(data_account):
				return
		elif (n=='2'):
			id_admin = input('Nhập mã người quản trị : ')
			if (id_admin == '123456'):
				ACCOUNT_MANAGE(data_account)
			else:
				print('\nMã người quản trị không hợp lệ !')
		elif (n=='3'):
			lua_chon = input('Bạn có muốn thoát không ? (Y/N) : ')
			if (lua_chon=='Y' or lua_chon=='y'):
				quit()

#đọc dữ liệu trong file
def READ_FILE(danh_sach_san_pham):
	open_data = open('data.txt','r')
	read_data = open_data.readlines()
	if (read_data==[]):
		open_data.close()
		return
	else:
		for i in read_data:
			danh_sach_san_pham.append(i.split())
		return

#hàm gồm chức năng dành cho người quản lý
def TINH_NANG_QUAN_LY(danh_sach_san_pham):
	#ghi dữ liệu vào file
	def WRITE_TO_FILE(danh_sach_san_pham):
		write_data = open('data.txt','w')
		for i in danh_sach_san_pham:
			for j in range(0,len(i)):
				write_data.writelines([i[j],' '])
			write_data.write('\n')
		write_data.close()

	#kiểm tra các sản phẩm khi nhập vào đã có trong trong kho hay chưa
	def KIEM_TRA_TRUNG_LAP(danh_sach_san_pham,tensp):
		for i in danh_sach_san_pham:
			if(tensp==i[0]):
				return False
		return True

	#hàm thêm 1 hoặc nhiều sản phẩm vào kho
	def THEM_SAN_PHAM(danh_sach_san_pham):
		while 1:
			danh_sach_con = list()
			tensp = input('nhập tên sản phẩm : ')
			if (KIEM_TRA_TRUNG_LAP(danh_sach_san_pham,tensp)):
				if (tensp!='') and (tensp.isspace()==False):
					danh_sach_con.append(tensp)
				else:
					while (tensp=='') or (tensp.isspace()):
						print('\ntên sản phẩm không được để trống')
						tensp = input('nhập tên sản phẩm : ')
						if (tensp!='') and (tensp.isspace()==False):
							danh_sach_con.append(tensp)
				gia_nhap = input('giá nhập của sp : ')
				if (gia_nhap.isdigit()):
					danh_sach_con.append(gia_nhap)
				else:
					while (not gia_nhap.isdigit()):
						print('\ngiá nhập không được âm hoặc có chữ cái !')
						gia_nhap = input('giá nhập của sp : ')
						if (gia_nhap.isdigit()):
							danh_sach_con.append(gia_nhap)
				gia_ban = input('giá bán của sp : ')
				if (gia_ban.isdigit()):
					danh_sach_con.append(gia_ban)
				else:
					while (not gia_ban.isdigit()):
						print('\ngiá bán không được âm hoặc có chữ cái !')
						gia_ban = input('giá bán của sp : ')
						if (gia_ban.isdigit()):
							danh_sach_con.append(gia_ban)
				so_luong = input('nhập số lương sản phẩm : ')
				if (so_luong.isdigit()):
					danh_sach_con.append(so_luong)
				else:
					while (not so_luong.isdigit()):
						print('\ngiá bán không được âm hoặc có chữ cái !')
						so_luong = input('giá bán của sp : ')
						if (so_luong.isdigit()):
							danh_sach_con.append(so_luong)
				danh_sach_san_pham.append(danh_sach_con)
				WRITE_TO_FILE(danh_sach_san_pham)
				n = input('bạn có muốn tiếp tục thêm sản phẩm không ? (Y/N) : ')
				if (n=='N' or n=='n'):
					return
			else:
				print('\nSản phẩm đã có trong kho !')
				return

	#hàm xóa 1 sản phẩm trong kho
	def XOA_SAN_PHAM(danh_sach_san_pham):
		while 1:
			san_pham_can_xoa = input('Nhập tên sản phẩm cần xóa : ')
			for i in danh_sach_san_pham:
				if (san_pham_can_xoa == i[0]):
					lua_chon = input(f'Bạn có chắc chắn muốn xóa sản phẩm "{san_pham_can_xoa}" không ? (Y/N) : ')
					if (lua_chon=='Y' or lua_chon=='y'):
						danh_sach_san_pham.remove(i)
						print('\nXóa sản phẩm thành công.')
						return
					else:
						print('\nSản phẩm đã được giữ lại.')
						return
			print('\nSản phẩm không tồn tại')
			return
	while 1:
		print('\n\t\t\t\t\t---MENU QUẢN LÝ---')
		print('\t\t1. Thêm sản phẩm')
		print('\t\t2. Xóa sản phẩm')
		print('\t\t3. In danh sách sản phẩm trong kho')
		print('\t\t4. Quay lại')
		n = input('nhập lựa chọn : ')
		if (n=='1'):
			THEM_SAN_PHAM(danh_sach_san_pham)
		elif (n=='2'):
			XOA_SAN_PHAM(danh_sach_san_pham)
		elif (n=='3'):
			IN_DANH_SACH(danh_sach_san_pham)
		elif (n=='4'):
			return
#hàm in danh sách các mặt hàng trong kho
def IN_DANH_SACH(danh_sach_san_pham):
	print('\n\t\t\t\t\t\t\t\t\t---DANH SÁCH SẢN PHẨM---')
	print('{:>20} {:>20} {:>20} {:>20}'.format('tên sản phẩm','giá nhập (VND)','giá bán (VND)','số lượng tồn'))
	for i in danh_sach_san_pham:
		for j in i:
			print(end='{:>20}'.format(j))
		print('\n')

#khu vực chính (main)
BEGIN()
danh_sach_san_pham = list()
READ_FILE(danh_sach_san_pham)
while 1:
	print('\n\t\t\t\t---MENU NHÂN VIÊN---')
	print('\t\t1. In danh sách sản phẩm trong kho')
	print('\t\t2. Tìm kiếm sản phẩm')
	print('\t\t3. Sắp xếp sản phẩm')
	print('\t\t4. Chức năng quản lý')
	print('\t\t5. Đăng xuất')
	n = input('nhập lựa chọn : ')
	if (n=='1'):
		IN_DANH_SACH(danh_sach_san_pham)
	elif (n=='2'):
		print('Chức năng chưa được phát triển')
	elif (n=='3'):
		print('Chức năng chưa được phát triển')
	elif (n=='4'):
		ID_quan_ly = input('Nhập mã người quản lý : ')
		if (ID_quan_ly=='123456'):
			TINH_NANG_QUAN_LY(danh_sach_san_pham)
		else:
			print('\nMã không hợp lệ !')
	elif (n=='5'):
		lua_chon = input('Bạn có đăng xuất không ? (Y/N) : ')
		if (lua_chon == 'Y' or lua_chon=='y'):
			BEGIN()
			