from mongoengine import *
# import mlab

# mlab.connect()

class Food(Document):
    ten_mon = StringField()
    chu_de = StringField()
    nguyen_lieu = ListField()
    link_anh = StringField()
    cach_lam = ListField(DictField())
    link_san_pham = StringField()


# new_food = Food(
#     link_san_pham = "http://imgs.vietnamnet.vn/Images/2017/08/31/16/20170831160446-mon-ngon-2-9-1.jpg",
#     chu_de = "family",
#     ten_mon = "Vịt om sấu",
#     nguyen_lieu = ["Nửa con vịt.", "Sấu: 7 - 12 quả (tùy theo vị chua nhiều hay ít).", "Rau muống hoặc rau rút.", "Khoai sọ: 200gr.", "Nước dừa: một quả. (không bắt buộc) Nhiều gia đình cho nước dừa vào để om sấu, sẽ giúp thịt vịt mềm và ngon hơn rất nhiều.", "Gia vị: chanh, muối, đường, gừng, hành củ, hành lá, xả, tỏi.", "Bún tươi ăn kèm."],
#     link_anh = "",
#     cach_lam = [
#         {
#             "mo_ta": "Sơ chế vịt bằng cách cho một ít muối vào vịt rồi dùng tay bóp cho sạch lông măng. Sau đó rửa sạch vịt với nước. Dùng một nửa quả chanh xát mạnh vào da vịt cho hết mùi tanh. Cuối cùng, lấy dao hoặc lấy kéo cắt vịt thành từng miếng nhỏ.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Ướp vịt với gia vị: đập dập, băm nhỏ hành củ, tỏi, xả, gừng rồi cho vào vịt, cho thêm một thìa cà phê muối, một thìa cà phê đường rồi lấy đũa đảo đều và ướp trong 30 phút cho gia vị ngấm vào vịt.",
#             "link": "",
#         },
#         {
#             "mo_ta": "Sau khoảng 30 phút khi vịt đã ngấm gia vị, cho vịt vào nồi, cho thêm một chút dầu ăn và xào chín sơ. Sau đó đổ nước vừa đủ. Cho thêm sấu vào nồi vịt và đun nhỏ lửa. Khoảng 30 phút, khi vịt đã chín mềm, bạn đổ khoai sợ vào và đun cho tới khi khoai chín bở rồi nêm gia vị cho vừa miệng.",
#             "link": "",
#         },
        
#     ]
# )

# new_food.save()