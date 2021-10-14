import os
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
		if (tai_khoan != '' and not tai_khoan.isspace()):
			mat_khau = input('Mật khẩu : ')
			if mat_khau != '' and not mat_khau.isspace():
				if (tai_khoan in data_account) and (data_account[tai_khoan] == mat_khau):
					os.system('cls||clear')
					return True
				else:
					os.system('cls||clear')
					print('Thông tin tài khoản hoặc mật khẩu chưa chính xác !\n')
					return False
			else:
				os.system('cls||clear')
				print('Bạn chưa điền mật khẩu !\n')
				return False
		else:
			os.system('cls||clear')
			print('Bạn chưa điền tài khoản đăng nhập !\n')
			return False

#hàm quản trị 
def ACCOUNT_MANAGE(data_account):

	#hàm ghi tài khoản vào trong file lưu trữ
	def WRITE_DATA_ACCOUNT(data_account):
		write_data = open('data_account.txt','w')
		for i in data_account.items():
			write_data.writelines([i[0],' ',i[1],'\n'])
		write_data.close()
	
	#hàm tạo 1 tài khoản mới
	def REGISTER(data_account):
		while 1:
			tai_khoan_moi = input('Tài khoản mới : ')
			if (tai_khoan_moi not in data_account and tai_khoan_moi != '' and not tai_khoan_moi.isspace()):
				while 1:
					mat_khau_moi = input('Mật khẩu : ')
					if (mat_khau_moi == '' or mat_khau_moi.isspace()):
						os.system('cls||clear')
						print('Mật khẩu không được để trống !\n')
						return
					else:
						data_account [tai_khoan_moi] = mat_khau_moi
						WRITE_DATA_ACCOUNT(data_account)
						os.system('cls||clear')
						print('Đăng ký tài khoản thành công.\n')
						return
			elif (tai_khoan_moi in data_account):
				os.system('cls||clear')
				print(f'Tài khoản "{tai_khoan_moi}" đã tồn tại !\n')
				return
			elif (tai_khoan_moi == '' or tai_khoan_moi.isspace()):
				os.system('cls||clear')
				print('Tài khoản đăng ký mới không được để trống !\n')
				return

	#hàm xóa tài khoản
	def DELETE_ACCOUNT(data_account):
		del_account = input('Nhập tài khoản cần xóa : ')
		if (del_account in data_account):
			while 1:
				select = input(f'Bạn có chắc chắn muốn xóa tài khoản "{del_account}" không ? (Y/N) : ')
				if (select == 'Y' or select == 'y'):
					del data_account[del_account]
					WRITE_DATA_ACCOUNT(data_account)
					os.system('cls||clear')
					print('Xóa tài khoản thành công.\n')
					print('\t=== DANH SÁCH SAU KHI XÓA TÀI KHOẢN ===')
					PRINT_DATA_ACCOUNT(data_account)
					return
				elif (select == 'N' or select == 'n'):
					os.system('cls||clear')
					print('Tài khoản đã được giữ lại.\n')
					return
		else:
			os.system('cls||clear')
			print(f'Tài khoản "{del_account}" không tồn tại !\n')
			return

	#hàm in danh sách các tài khoản có trong hệ thống
	def PRINT_DATA_ACCOUNT(data_account):
		print('{:>20} {:>20}'.format('Tài khoản','Mật khẩu','\n'))
		for i in data_account.items():
			print('{:>20} {:>20}'.format(*i))
			print('\n')
	while 1:
		print('\t\t=== MENU QUẢN LÝ TÀI KHOẢN ===')
		print('\t\t1. Đăng ký')
		print('\t\t2. Xóa tài khoản')
		print('\t\t3. Hiển thị danh sách tài khoản')
		print('\t\t4. Quay lại')
		lua_chon = input('Mời bạn nhập lựa chọn : ')
		if (lua_chon=='1'):
			os.system('cls||clear')
			print('=== ĐĂNG KÝ TÀI KHOẢN ===')
			REGISTER(data_account)
		elif (lua_chon=='2'):
			os.system('cls||clear')
			print('\t=== DANH SÁCH TÀI KHOẢN VÀ MẬT KHẨU HIỆN CÓ ===')
			PRINT_DATA_ACCOUNT(data_account)
			print('=== XÓA TÀI KHOẢN ===')
			DELETE_ACCOUNT(data_account)
		elif (lua_chon=='3'):
			os.system('cls||clear')
			print('\t=== DANH SÁCH TÀI KHOẢN VÀ MẬT KHẨU ===\n')
			PRINT_DATA_ACCOUNT(data_account)
		elif (lua_chon=='4'):
			os.system('cls||clear')
			return
		else:
			os.system('cls||clear')

#hàm đăng nhập chạy đầu tiên khi mở chương trình
def BEGIN():
	data_account = dict()
	READ_DATA_ACCOUNT(data_account)
	while 1:
		print('\t\t\t==== PHẦN MỀM QUẢN LÝ CÁC MẪU ĐIỆN THOẠI TRONG KHO ====')
		print('\t\t1. Đăng nhập')
		print('\t\t2. Quản lý tài khoản')
		print('\t\t3. Thoát chương trình')
		lua_chon = input('Nhập lựa chọn : ')
		if (lua_chon=='1'):
			os.system('cls||clear')
			print('=== ĐĂNG NHẬP ===')
			if LOGIN(data_account):
				return
		elif (lua_chon=='2'):
			os.system('cls||clear')
			id_admin = input('Nhập mã người quản trị : ')
			if (id_admin == '123456'):
				os.system('cls||clear')
				ACCOUNT_MANAGE(data_account)
			else:
				os.system('cls||clear')
				print('Mã người quản trị không hợp lệ !\n')
		elif (lua_chon=='3'):
			os.system('cls||clear')
			quit()
		else:
			os.system('cls||clear')

#đọc dữ liệu trong file
def READ_FILE(danh_sach_san_pham):
	open_data = open('data.txt','r')
	read_data = open_data.readlines()
	if (read_data==[]):
		open_data.close()
		return
	else:
		for i in read_data:
			j = i.split()
			for k in range(0,len(j)):
				if (j[k].isdigit()):
					j[k] = int(j[k])
			danh_sach_san_pham.append(j)
		open_data.close()
		return

#hàm gồm chức năng dành cho người quản lý
def TINH_NANG_QUAN_LY(danh_sach_san_pham):
	#ghi dữ liệu vào file
	def WRITE_TO_FILE(danh_sach_san_pham):
		write_data = open('data.txt','w')
		for i in danh_sach_san_pham:
			for j in range(0,len(i)):
				write_data.writelines([str(i[j]),' '])
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
			masp = input('Nhập mã sản phẩm : ')
			if (KIEM_TRA_TRUNG_LAP(danh_sach_san_pham,masp)):
				if (masp!='') and (masp.isspace()==False):
					danh_sach_con.append(masp.upper())
				else:
					os.system('cls||clear')
					print('Mã sản phẩm không được để trống !\n')
					return
				tensp = input('Nhập tên sản phẩm : ')
				if (tensp!='') and (tensp.isspace()==False):
					danh_sach_con.append(tensp)
				else:
					os.system('cls||clear')
					print('Tên sản phẩm không được để trống !\n')
					return
				gia_nhap = input('Giá nhập của sản phẩm : ')
				if (gia_nhap.isdigit()):
					danh_sach_con.append(int(gia_nhap))
				elif (gia_nhap=='' or gia_nhap.isspace()):
					os.system('cls||clear')
					print('Giá nhập không được để trống !\n')
					return
				else:
					os.system('cls||clear')
					print('Giá nhập không được âm hoặc có kí tự đặng biệt !\n')
					return
				gia_ban = input('Giá bán của sản phẩm : ')
				if (gia_ban.isdigit()):
					danh_sach_con.append(int(gia_ban))
				elif (gia_ban=='' or gia_ban.isspace()):
					os.system('cls||clear')
					print('Giá bán không được để trống !\n')
					return
				else:
					os.system('cls||clear')
					print('Giá bán không được âm hoặc có kí tự đặng biệt !\n')
					return
				so_luong = input('Nhập số lương sản phẩm : ')
				if (so_luong.isdigit()):
					danh_sach_con.append(int(so_luong))
				elif (so_luong=='' or so_luong.isspace()):
					os.system('cls||clear')
					print('Số lương không được để trống !\n')
					return
				else:
					os.system('cls||clear')
					print('Số lương không được âm hoặc có kí tự đặng biệt !\n')
					return
				danh_sach_san_pham.append(danh_sach_con)
				WRITE_TO_FILE(danh_sach_san_pham)
				os.system('cls||clear')
				print(f'Thêm sản phẩm "{tensp}" thành công !\n')
				return
			else:
				os.system('cls||clear')
				print(f'Mã phẩm "{masp}" bị trùng lặp !\n')
				return

	#hàm xóa 1 sản phẩm trong kho
	def XOA_SAN_PHAM(danh_sach_san_pham):
		while 1:
			san_pham_can_xoa = input('Nhập mã sản phẩm cần xóa : ')
			for i in danh_sach_san_pham:
				if (san_pham_can_xoa.upper() == i[0]):
					while 1:
						xac_nhan = input(f'Bạn có chắc chắn muốn xóa sản phẩm "{i[1]}" với mã "{san_pham_can_xoa.upper()}" không ? (Y/N) : ')
						if (xac_nhan=='Y' or xac_nhan=='y'):
							danh_sach_san_pham.remove(i)
							WRITE_TO_FILE(danh_sach_san_pham)
							os.system('cls||clear')
							print(f'Xóa sản phẩm thành công.\n')
							print('\n\t\t\t\t======DANH SÁCH SAU KHI XÓA SẢN PHẨM======\n')
							IN_DANH_SACH(danh_sach_san_pham)
							return
						elif (xac_nhan=='N' or xac_nhan=='n'):
							os.system('cls||clear')
							print(f'Sản phẩm đã được giữ lại.\n')
							return
			os.system('cls||clear')
			print(f'Mã sản phẩm "{san_pham_can_xoa.upper()}" không tồn tại !\n')
			return
	def THAY_DOI_THONG_TIN(danh_sach_san_pham):
		def IN_DANH_SACH_CON(i):
			print('\n\t\t\t\t======DANH SÁCH SẢN PHẨM======\n')
			print('{:>20} {:>20} {:>20} {:>20} {:>20}'.format('Mã sản phẩm','Tên sản phẩm','Giá nhập (VND)','Giá bán (VND)','Số lượng tồn'),'\n')
			print('{:>20} {:>20} {:>20} {:>20} {:>20}\n'.format(*i))
		os.system('cls||clear')
		print('\n\t\t\t\t======DANH SÁCH SẢN PHẨM======\n')
		IN_DANH_SACH(danh_sach_san_pham)
		san_pham_can_doi = input('Nhập mã sản phẩm cần thay đổi thông tin: ')
		for i in danh_sach_san_pham:
			if (san_pham_can_doi.upper() == i[0]):
				os.system('cls||clear')
				while 1:
					IN_DANH_SACH_CON(i)
					print('===LỰA CHỌN THAY ĐỔI===')
					print('1. Thay đổi tên của sản phẩm')
					print('2. Thay đổi giá nhập của sản phẩm')
					print('3. Thay đổi giá bán của sản phẩm')
					print('4. Thay đổi số lượng tồn kho của sản phẩm')
					print('5. Quay lại')
					lua_chon = input('Nhập lựa chọn : ')
					if (lua_chon=='1'):
						os.system('cls||clear')
						IN_DANH_SACH_CON(i)
						ten_moi = input('Cập nhật tên mới cho sản phẩm : ')
						if(ten_moi!='' and not ten_moi.isspace()):
							while 1:
								os.system('cls||clear')
								check = input(f'Bạn có chắc chắn muốn thay đổi tên sản phẩm thành "{ten_moi}" không ? (Y/N) : ')
								if (check == 'Y' or check == 'y'):
									i[1] = ten_moi
									os.system('cls||clear')
									print('Thay đổi tên của sản phẩm thành công.')
									break
								elif (check == 'N' or check == 'n'):
									os.system('cls||clear')
									print('Tên sản phẩm vẫn được giữ nguyên')
									break
								else:
									os.system('cls||clear')
						else:
							os.system('cls||clear')
							print('Tên của sản phẩm không được để trống !')
					elif (lua_chon=='2'):
						os.system('cls||clear')
						IN_DANH_SACH_CON(i)
						gia_nhap_moi = input('Cập nhật giá nhập mới : ')
						if(gia_nhap_moi!='' and not gia_nhap_moi.isspace() and gia_nhap_moi.isdigit()):
							while 1:
								os.system('cls||clear')
								check = input(f'Bạn có chắc chắn muốn thay đổi giá nhập của sản phẩm thành "{gia_nhap_moi}" không ? (Y/N) : ')
								if (check == 'Y' or check == 'y'):
									i[2] = gia_nhap_moi
									os.system('cls||clear')
									print('Thay đổi giá nhập của sản phẩm thành công.')
									break
								elif (check == 'N' or check == 'n'):
									os.system('cls||clear')
									print('Giá nhập của sản phẩm vẫn được giữ nguyên')
									break
								else:
									os.system('cls||clear')
						elif (gia_nhap_moi=='' or gia_nhap_moi.isspace()):
							os.system('cls||clear')
							print('Giá nhập của sản phẩm không được để trống !')
						else:
							os.system('cls||clear')
							print('Giá nhập không được âm hoặc chứa kí tự đặc biệt !')
					elif (lua_chon=='3'):
						os.system('cls||clear')
						IN_DANH_SACH_CON(i)
						gia_ban_moi = input('Cập nhật giá bán mới : ')
						if(gia_ban_moi!='' and not gia_ban_moi.isspace() and gia_ban_moi.isdigit()):
							while 1:
								os.system('cls||clear')
								check = input(f'Bạn có chắc chắn muốn thay đổi giá bán của sản phẩm thành "{gia_ban_moi}" không ? (Y/N) : ')
								if (check == 'Y' or check == 'y'):
									i[3] = gia_ban_moi
									os.system('cls||clear')
									print('Thay đổi giá bán của sản phẩm thành công.')
									break
								elif (check == 'N' or check == 'n'):
									os.system('cls||clear')
									print('Giá bán của sản phẩm vẫn được giữ nguyên')
									break
								else:
									os.system('cls||clear')
						elif (gia_ban_moi=='' or gia_ban_moi.isspace()):
							os.system('cls||clear')
							print('Giá bán của sản phẩm không được để trống !')
						else:
							os.system('cls||clear')
							print('Giá bán không được âm hoặc chứa kí tự đặc biệt !')
					elif (lua_chon=='4'):
						os.system('cls||clear')
						IN_DANH_SACH_CON(i)
						so_luong_moi = input('Thay đổi số lượng tồn : ')
						if(so_luong_moi!='' and not so_luong_moi.isspace() and so_luong_moi.isdigit()):
							while 1:
								os.system('cls||clear')
								check = input(f'Bạn có chắc chắn muốn thay đổi số lượng của sản phẩm thành "{so_luong_moi}" không ? (Y/N) : ')
								if (check == 'Y' or check == 'y'):
									i[4] = so_luong_moi
									os.system('cls||clear')
									print('Thay đổi số lượng của sản phẩm thành công.')
									break
								elif (check == 'N' or check == 'n'):
									os.system('cls||clear')
									print('Số lượng của sản phẩm vẫn được giữ nguyên')
									break
								else:
									os.system('cls||clear')
						elif (so_luong_moi=='' or so_luong_moi.isspace()):
							os.system('cls||clear')
							print('số lượng tồn của sản phẩm không được để trống !')
						else:
							os.system('cls||clear')
							print('số lượng tồn không được âm hoặc chứa kí tự đặc biệt !')
					elif (lua_chon=='5'):
						WRITE_TO_FILE(danh_sach_san_pham)
						os.system('cls||clear')
						return
					else:
						os.system('cls||clear')
		os.system('cls||clear')
		print(f'Mã sản phẩm "{san_pham_can_doi}" không tồn tại !')
		return
	while 1:
		print('\n\t\t=== MENU QUẢN LÝ ===')
		print('\t\t1. Thêm sản phẩm')
		print('\t\t2. Thay đổi thông tin sản phẩm')
		print('\t\t3. Xóa sản phẩm')
		print('\t\t4. Tìm kiếm sản phẩm')
		print('\t\t5. Sắp xếp sản phẩm')
		print('\t\t6. In danh sách sản phẩm trong kho')
		print('\t\t7. Quay lại')
		lua_chon = input('nhập lựa chọn : ')
		if (lua_chon=='1'):
			os.system('cls||clear')
			print('=== THÊM SẢN PHẨM ===')
			THEM_SAN_PHAM(danh_sach_san_pham)
		elif (lua_chon=='2'):
			THAY_DOI_THONG_TIN(danh_sach_san_pham)
		elif (lua_chon=='3'):
			os.system('cls||clear')
			print('\n\t\t\t======DANH SÁCH SẢN PHẨM ĐANG CÓ TRONG KHO======\n')
			IN_DANH_SACH(danh_sach_san_pham)
			print('=== XÓA SẢN PHẨM ===')
			XOA_SAN_PHAM(danh_sach_san_pham)
		elif (lua_chon=='4'):
			os.system('cls||clear')
			TIM_KIEM_SAN_PHAM(danh_sach_san_pham)
		elif (lua_chon=='5'):
			os.system('cls||clear')
			SAP_XEP_DANH_SACH(danh_sach_san_pham)
		elif (lua_chon=='6'):
			os.system('cls||clear')
			print('\n\t\t\t\t======DANH SÁCH SẢN PHẨM======\n')
			IN_DANH_SACH(danh_sach_san_pham)
		elif (lua_chon=='7'):
			os.system('cls||clear')
			return
		else:
			os.system('cls||clear')

#hàm in danh sách các mặt hàng trong kho
def IN_DANH_SACH(danh_sach_san_pham):
	print('{:>20} {:>20} {:>20} {:>20} {:>20}'.format('Mã sản phẩm','Tên sản phẩm','Giá nhập (VND)','Giá bán (VND)','Số lượng tồn'),'\n')
	for i in danh_sach_san_pham:
		print('{:>20} {:>20} {:>20} {:>20} {:>20}'.format(*i))
		print('\n')

#hàm chứa các chức năng tìm kiếm
def TIM_KIEM_SAN_PHAM(danh_sach_san_pham):
	#hàm tìm kiếm sản phẩm theo lựa chọn
	def TIM_KIEM(danh_sach_san_pham,lua_chon):
		tu_khoa = input('Nhập thông tin cần tìm : ')
		if (tu_khoa!='' and not tu_khoa.isspace()):
			danh_sach_tim_kiem = list()
			for i in danh_sach_san_pham:
				if (tu_khoa==str(i[lua_chon])):
					danh_sach_tim_kiem.append(i)
			if (danh_sach_tim_kiem==[]):
				os.system('cls||clear')
				print('Thông tin sản phẩm không có trong danh sách !\n')
				return
			else:
				os.system('cls||clear')
				print('\t\t\t\t====DANH SÁCH KẾT QUẢ TÌM KIẾM====')
				IN_DANH_SACH(danh_sach_tim_kiem)
		else:
			os.system('cls||clear')
			print('Bạn chưa nhập thông tin tìm kiếm !\n')
			return
	while 1:
		print('\n\t\t=== TÌM KIẾM / LỌC SẢN PHẨM ===')
		print('\t\t1. Tìm kiếm theo mã sản phẩm')
		print('\t\t2. Tìm kiếm theo tên sản phẩm')
		print('\t\t3. Lọc các sản phẩm có cùng giá nhập')
		print('\t\t4. Lọc các sản phẩm có cùng giá bán')
		print('\t\t5. Lọc các sản phẩm có cùng số lượng tồn')
		print('\t\t6. Quay lại')
		lua_chon = input('nhập lựa chọn : ')
		if (lua_chon=='1'):
			os.system('cls||clear')
			print('===TÌM KIẾM THEO MÃ SẢN PHẨM===')
			TIM_KIEM(danh_sach_san_pham,int(lua_chon)-1)
		elif (lua_chon=='2'):
			os.system('cls||clear')
			print('===TÌM KIẾM THEO TÊN SẢN PHẨM===')
			TIM_KIEM(danh_sach_san_pham,int(lua_chon)-1)
		elif (lua_chon=='3'):
			os.system('cls||clear')
			print('===LỌC CÁC SẢN PHẨM CÓ CÙNG GIÁ NHẬP===')
			TIM_KIEM(danh_sach_san_pham,int(lua_chon)-1)
		elif (lua_chon=='4'):
			os.system('cls||clear')
			print('===LỌC CÁC SẢN PHẨM CÓ CÙNG GIÁ BÁN===')
			TIM_KIEM(danh_sach_san_pham,int(lua_chon)-1)
		elif (lua_chon=='5'):
			os.system('cls||clear')
			print('===LỌC CÁC SẢN PHẨM CÓ CÙNG SỐ LƯỢNG TỒN===')
			TIM_KIEM(danh_sach_san_pham,int(lua_chon)-1)
		elif (lua_chon=='6'):
			os.system('cls||clear')
			return
		else:
			os.system('cls||clear')

#hàm sắp xếp danh sách
def SAP_XEP_DANH_SACH(danh_sach_san_pham):
	#hàm sắp xếp theo tùy chọn
	def SAP_XEP (danh_sach_san_pham,lua_chon,tuy_chon):
		#hàm xử lý tùy chọn
		def TUY_CHON(phan_tu):
				return phan_tu[lua_chon]
		if (tuy_chon=='1'):
			IN_DANH_SACH(sorted(danh_sach_san_pham,key=TUY_CHON))
		elif (tuy_chon=='2'):
			IN_DANH_SACH(sorted(danh_sach_san_pham,key=TUY_CHON,reverse=True))
	while 1:
		print('\n\t\t=== SẮP XẾP SẢN PHẨM ===')
		print('\t\t1. Sắp xếp theo tên sản phẩm')
		print('\t\t2. Sắp xếp theo giá nhập')
		print('\t\t3. Sắp xếp theo giá bán')
		print('\t\t4. Sắp xếp theo số lượng tồn')
		print('\t\t5. Quay lại')
		lua_chon = input('nhập lựa chọn : ')
		if (lua_chon=='1'):
			os.system('cls||clear')
			while 1:
				print('1. Sắp xếp tăng dần.')
				print('2. Sắp xếp giảm dần.')
				tuy_chon = input('Mời bạn chọn kiểu sắp xếp : ')
				if (tuy_chon=='1'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO TÊN SẢN PHẨM (A - Z)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				elif (tuy_chon=='2'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO TÊN SẢN PHẨM (Z - A)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				else:
					os.system('cls||clear')
		elif (lua_chon=='2'):
			os.system('cls||clear')
			while 1:
				print('1. Sắp xếp tăng dần.')
				print('2. Sắp xếp giảm dần.')
				tuy_chon = input('Mời bạn chọn kiểu sắp xếp : ')
				if (tuy_chon=='1'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO GIÁ NHẬP (TĂNG DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				elif (tuy_chon=='2'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO GIÁ NHẬP (GIẢM DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				else:
					os.system('cls||clear')
		elif (lua_chon=='3'):
			os.system('cls||clear')
			while 1:
				print('1. Sắp xếp tăng dần.')
				print('2. Sắp xếp giảm dần.')
				tuy_chon = input('Mời bạn chọn kiểu sắp xếp : ')
				if (tuy_chon=='1'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO GIÁ BÁN (TĂNG DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				elif (tuy_chon=='2'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO GIÁ BÁN (GIẢM DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				else:
					os.system('cls||clear')
		elif (lua_chon=='4'):
			os.system('cls||clear')
			while 1:
				print('1. Sắp xếp tăng dần.')
				print('2. Sắp xếp giảm dần.')
				tuy_chon = input('Mời bạn chọn kiểu sắp xếp : ')
				if (tuy_chon=='1'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO SỐ LƯỢNG TỒN (TĂNG DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				elif (tuy_chon=='2'):
					print('\n\t\t\t======DANH SÁCH SẮP XẾP THEO SỐ LƯỢNG TỒN (GIẢM DẦN)======\n')
					SAP_XEP (danh_sach_san_pham,int(lua_chon),tuy_chon)
					break
				else:
					os.system('cls||clear')
		elif (lua_chon=='5'):
			os.system('cls||clear')
			return
		else:
			os.system('cls||clear')

#khu vực chính (main)
BEGIN()
danh_sach_san_pham = list()
READ_FILE(danh_sach_san_pham)
while 1:
	print('\n\t\t\t=== MENU NHÂN VIÊN ===')
	print('\t\t1. In danh sách sản phẩm trong kho')
	print('\t\t2. Tìm kiếm sản phẩm')
	print('\t\t3. Sắp xếp sản phẩm')
	print('\t\t4. Chức năng quản lý')
	print('\t\t5. Đăng xuất')
	lua_chon = input('nhập lựa chọn : ')
	if (lua_chon=='1'):
		os.system('cls||clear')
		print('\n\t\t\t\t======DANH SÁCH SẢN PHẨM======\n')
		IN_DANH_SACH(danh_sach_san_pham)
	elif (lua_chon=='2'):
		os.system('cls||clear')
		TIM_KIEM_SAN_PHAM(danh_sach_san_pham)
	elif (lua_chon=='3'):
		os.system('cls||clear')
		SAP_XEP_DANH_SACH(danh_sach_san_pham)
	elif (lua_chon=='4'):
		os.system('cls||clear')
		ID_quan_ly = input('Nhập mã người quản lý : ')
		if (ID_quan_ly=='123456'):
			os.system('cls||clear')
			TINH_NANG_QUAN_LY(danh_sach_san_pham)
		else:
			os.system('cls||clear')
			print('Mã không hợp lệ !')
	elif (lua_chon=='5'):
		os.system('cls||clear')
		while 1:
			xac_nhan = input('Bạn có muốn đăng xuất không ? (Y/N) : ')
			if (xac_nhan == 'Y' or xac_nhan == 'y'):
				os.system('cls||clear')
				BEGIN()
				break
			elif (xac_nhan == 'N' or xac_nhan == 'n'):
				os.system('cls||clear')
				break
	else:
		os.system('cls||clear')