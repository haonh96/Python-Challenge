#0. Challenge0 => Tính 2**38 = 274877906944 => changllenge tiếp:
http://www.pythonchallenge.com/pc/def/274877906944.html
---------------------------------------------------------------------
1. Challenge1: Link: http://www.pythonchallenge.com/pc/def/map.html
	Chính xác đây code thuật toán mã hóa cessar với k=2 để giải mã đoạn thông điệp
	Code đính kèm: file challenge01.py
	=> Link bài challenge2:  http://www.pythonchallenge.com/pc/def/ocr.html
---------------------------------------------------------------------
	#2. Challange2: Bài này gợi ý dẫn ta đến việc chú ý đến source code. Trong soucre của bài có dòng comment với gới ý tìm các ký tự có nghĩa trong đống lộn xộn các ký tự. Ta sẽ viết code để giải quyết bài toán này. Code sẽ nằm ở challenge02.py ta được chuỗi ký tự có nghĩa là : equality
	=> Link bài challnge3: http://www.pythonchallenge.com/pc/def/equality.html
---------------------------------------------------------------------
#3. Challange3: http://www.pythonchallenge.com/pc/def/equality.html
	Vào trang này ta thấy gợi ý One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
	Tức dịch là có 1 chữ nhỏ được bao bọc bởi 3 chữ lớn bên ngoài. View source ta thấy 1 đoạn comment html chứa 1 chuỗi string lộn xộn => Mình phải tìm các từ có trong đống lộn xộn này thỏa mã các yêu cầu nói trên. Và tất nhiên để tìm kiếm 1 cách nhanh nhất ta sẽ dùng regex.
	Ta có code bài này ở : challenge03.py
	Ta được từ khóa : linkedlist
	=> Link challenge05: http://www.pythonchallenge.com/pc/def/linkedlist.html
---------------------------------------------------------------------
#4. Challenge4: http://www.pythonchallenge.com/pc/def/linkedlist.html
	Vào trang viewsource ta thấy có gợi ý nên brouforce trang http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345. Chắc sẽ bruoteforce biến nothing nào đến 1 giá trị mà server chấp nhận
	Ta có code bài giải ở: challenge04.py Ta thu được : peak.html
---------------------------------------------------------------------
#5. challenge05: http://www.pythonchallenge.com/pc/def/peak.html

	Truy cập vào link viewsource code ta thấy <!-- peak hell sounds familiar ? --> . Tức ở đây có nghĩa là từ tiếng anh có phát âm tương tự tạm thời chưa biết từ đó là từ gì???. Ta thấy trong source có thẻ <peakhell src="banner.p"/> Thẻ này lấy src là banner.p nên ta thử đọc xem nó là cái gì:
	Ta đọc nội dung của file banner.p có phần đầu là:
	(lp0\n(lp1\n(S' '\np2\
	Mấy dòng đầu khiến ta liên tưởng đến thư viện pickle , thư viện này sẽ dump list ra file dưới định dạng giống như thế này. Do đó ta sẽ dùng thử viện này để load pickle đã dump.
	Và in mảng ra đó ta được từ khóa channel
	=> có link challenge tiếp theo là http://www.pythonchallenge.com/pc/def/channel.html
---------------------------------------------------------------------

#6. Challenge06: http://www.pythonchallenge.com/pc/def/channel.html
	viewsource ta thấy comment zip => ta thử link http://www.pythonchallenge.com/pc/def/channel.zip ta down được file channel.zip về extract ra ta thấy nó là tập hợp các file. Mở 1 file ta thấy có nội dung là:
	Next nothing is 83831
	Kiểu dạng bài này khá giống với challenge4 chỉ khác ở đây ta phải xử lý với file mà thôi. Ta sẽ viết code đọc lần lượt theo thứ tự các con số này đến khi có được kết quả thì thôi
	Code của challenge này là challenge06.py
	Ta lấy được challenge tiếp theo là  oxygen
---------------------------------------------------------------------

#7. Challenge07: http://www.pythonchallenge.com/pc/def/oxygen.html
	Bài này khi truy cập vào sẽ không có gì khác ngoài một bức ảnh. Bức ảnh này có điểm bất thường là phần giữa bức ảnh bị nhòe không rõ. Suy ra đoạn giữa này rất có thể đã bị thay đổi pixel chứa một thông điệp bí mật nào đó.Để đọc pixel file ảnh ta có thể dùng thư viện pillow trong python
	Ta có code vượt qua challenge này ở: challenge07.py
	Đầu tiên ta sẽ viết đoạn chương trình nhỏ đọc tất cả các pixel bất thường ở giữa của ảnh

	Ta thu duoc ket qua : smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
	Dich ra ta duoc ket qua cuoi cung: integrity


---------------------------------------------------------------------
#8. challenge08: http://www.pythonchallenge.com/pc/def/integrity.html
	Challenge này khá thú vị: Đầu tiên khi vào trang web ta thấy 1 bức tranh chú ong đang hút mật:
	Viewsource lên ta thấy 2 dòng khá thú vị:

	<!--
	un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
	-->

	Ta đưa các ký tự BZ91 lên google để tìm kiếm thì phát hiện đây là định dạng bz2. Ta sẽ sử dụng thư viện bz2 trong python để decode. 
	import bz2
	print(bz2(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
	=> hunge
	print(bz2(b''BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08''))
	=> file
	-> user name=huge, pass=file
	=> changle 9: http://www.pythonchallenge.com/pc/return/good.html;

#9. Challenge9: http://www.pythonchallenge.com/pc/return/good.html;
	Challenge này khi view suorce lên ta thấy 2 giá trị first second nhưng k biết để làm gì. Nhưng nhìn vào bức tranh đầu bài bị vài chi tiết chấm đen, nên khả năng cao sẽ liên quan đến xử lý ảnh. Do đó việc còn lại ta thử vẽ ảnh từ các pixel đã được cho trước first và second
	vẽ hình tra thấy hình con bò là cow = . link next challenge cow.html
	Tuy nhiên lúc chúng ta truy cập sẽ hiện thị thông báo chỉ đó là con bò đực => bull.html

10. 