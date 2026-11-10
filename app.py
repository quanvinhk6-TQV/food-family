import streamlit as st
import os

class FoodExpertSystem:
    def __init__(self):
        # 1. Tập sự kiện - Danh sách các món ăn kèm mô tả chi tiết
        self.dishes = {
            "K1": {
                "name": "Cháo thịt bằm",
                "desc": "Cháo thịt bằm là món ăn được chế biến từ gạo và thịt heo băm nhỏ, nấu cùng nước đến khi cháo mềm nhừ. Món ăn có hương vị thanh nhẹ, dễ ăn, có thể kết hợp với hành lá, tiêu hoặc rau thơm tùy khẩu vị. Đây là món nước phù hợp dùng vào bữa sáng hoặc bữa tối. Chi phí ước tính dưới 30.000 đồng, thời gian chuẩn bị trên 30 phút."
            },
            "K2": {
                "name": "Phở gà",
                "desc": "Phở gà là món ăn được chế biến từ bánh phở, thịt gà và nước dùng ninh từ xương gà, kết hợp với hành lá, rau thơm. Món ăn có hương vị thanh nhẹ, thơm ngon, nước dùng đậm đà. Phù hợp dùng vào bữa sáng hoặc bữa trưa, chi phí từ 30.000–50.000 đồng, thời gian trên 30 phút."
            },
            "K3": {
                "name": "Bún riêu cua",
                "desc": "Bún riêu cua là món ăn chế biến từ bún tươi, riêu cua đồng và nước dùng nấu cùng cà chua, đậu phụ. Món ăn có hương vị chua ngọt, đậm đà, nước dùng thơm ngon. Phù hợp dùng vào bữa sáng hoặc bữa trưa, chi phí từ 30.000–50.000 đồng, thời gian trên 30 phút."
            },
            "K4": {
                "name": "Bún bò Huế",
                "desc": "Bún bò Huế mang đậm nét đặc trưng ẩm thực miền Trung, nổi bật với sợi bún to, nước dùng thơm mùi sả, vị đậm đà hòa quyện cùng vị cay nồng của sa tế. Chế biến từ thịt bò, giò heo, ăn kèm rau sống. Thời gian trên 30 phút, chi phí từ 30.000–50.000 đồng."
            },
            "K5": {
                "name": "Canh chua cá diêu hồng",
                "desc": "Canh chua cá diêu hồng nổi bật với vị chua thanh của me, vị ngọt tự nhiên từ cá và sự tươi mát của các loại rau như cà chua, thơm, đậu bắp, bạc hà. Thích hợp dùng vào bữa trưa hoặc bữa tối, thời gian trên 30 phút, chi phí từ 30.000–50.000 đồng."
            },
            "K6": {
                "name": "Cơm chiên trứng",
                "desc": "Cơm chiên trứng là món ăn đơn giản, hấp dẫn với hạt cơm tơi mềm, trứng gà béo thơm. Thành phẩm có màu vàng óng đẹp mắt, vị béo nhẹ không ngấy. Thời gian chế biến dưới 15 phút, chi phí dưới 30.000 đồng, thích hợp mọi bữa ăn."
            },
            "K7": {
                "name": "Cơm rang dưa bò",
                "desc": "Cơm rang dưa bò hấp dẫn với hạt cơm rang tơi giòn nhẹ, thịt bò mềm thơm và dưa cải muối chua dịu giúp món ăn không bị ngấy. Thời gian chuẩn bị 15–30 phút, chi phí từ 30.000–50.000 đồng."
            },
            "K8": {
                "name": "Cơm sườn nướng",
                "desc": "Cơm sườn nướng gồm miếng sườn heo tẩm ướp gia vị như mật ong, tỏi, hành rồi nướng vàng thơm, cạnh hơi xém. Thịt sườn mềm mọng, đậm vị mặn ngọt, ăn kèm cơm trắng và dưa leo. Thời gian trên 30 phút, chi phí 30.000–50.000 đồng."
            },
            "K9": {
                "name": "Bún thịt nướng",
                "desc": "Bún thịt nướng kết hợp bún tươi mềm mát, thịt heo tẩm ướp nướng vàng thơm và các loại rau sống xanh tươi, đậu phộng rang, nước mắm chua ngọt. Thích hợp dùng vào bữa sáng, thời gian trên 30 phút, chi phí 30.000–50.000 đồng."
            },
            "K10": {
                "name": "Cá sốt cà chua",
                "desc": "Cá sốt cà chua dân dã, thơm ngon với thịt cá mềm ngọt om cùng sốt cà chua đỏ au sánh nhẹ, đậm vị chua ngọt tự nhiên. Thích hợp dùng bữa trưa hoặc tối, thời gian 15–30 phút, chi phí 30.000–50.000 đồng."
            },
            "K11": {
                "name": "Gỏi gà rau củ",
                "desc": "Gỏi gà rau củ thanh mát với thịt gà luộc xé sợi trộn cùng rau củ tươi giòn (bắp cải, cà rốt, dưa leo) và nước sốt chua ngọt, rắc đậu phộng bùi béo. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K12": {
                "name": "Cá diêu hồng chiên xù",
                "desc": "Cá diêu hồng chiên xù có lớp vỏ vàng ruộm, giòn rụm bao bọc phần thịt cá trắng mềm bên trong. Ăn kèm rau sống và nước mắm chua ngọt. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K13": {
                "name": "Cánh gà chiên nước mắm",
                "desc": "Cánh gà chiên nước mắm thơm ngon với lớp da vàng giòn, phần thịt bên trong mềm mọng thấm đều sốt nước mắm tỏi đường đậm đà. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K14": {
                "name": "Đậu phụ chiên sả ớt",
                "desc": "Đậu phụ chiên sả ớt dân dã với những miếng đậu giòn bên ngoài, mềm béo bên trong, rang cùng sả băm và ớt tươi thơm nồng cay nhẹ. Chi phí dưới 30.000 đồng, thời gian 15–30 phút."
            },
            "K15": {
                "name": "Trứng chiên hành",
                "desc": "Trứng chiên hành quen thuộc, màu vàng óng của trứng hòa quyện với hành lá tươi xanh, vị béo nhẹ mềm xốp. Thời gian chế biến dưới 15 phút, chi phí dưới 30.000 đồng."
            },
            "K16": {
                "name": "Thịt ba chỉ luộc",
                "desc": "Thịt ba chỉ luộc kết hợp hài hòa giữa phần nạc mềm ngọt và lớp mỡ béo vừa phải, thái lát mỏng chấm kèm nước mắm tỏi ớt hoặc mắm nêm và rau sống. Thời gian 15–30 phút, chi phí 30.000–50.000 đồng."
            },
            "K17": {
                "name": "Rau muống luộc",
                "desc": "Rau muống luộc tươi xanh, giữ được độ giòn nhẹ và vị ngọt tự nhiên, chấm cùng nước mắm tỏi ớt. Thời gian dưới 15 phút, chi phí dưới 30.000 đồng, rất thanh mát."
            },
            "K18": {
                "name": "Rau củ luộc",
                "desc": "Rau củ luộc thanh đạm gồm cà rốt, súp lơ, đậu que, su su luộc chín tới giữ màu sắc tự nhiên và vị ngọt vốn có. Chấm muối tiêu chanh hoặc kho quẹt. Thời gian 15–30 phút, chi phí dưới 30.000 đồng."
            },
            "K19": {
                "name": "Trứng luộc",
                "desc": "Trứng luộc đơn giản, giàu dinh dưỡng với lòng trắng mềm mịn và lòng đỏ bùi béo. Thời gian nấu nhanh dưới 15 phút, chi phí dưới 30.000 đồng."
            },
            "K20": {
                "name": "Gà luộc",
                "desc": "Gà luộc truyền thống với thịt ngọt mềm, da vàng óng, chặt miếng bày đĩa rắc lá chanh thái sợi, chấm muối tiêu chanh. Thời gian trên 30 phút, chi phí trên 50.000 đồng."
            },
            "K21": {
                "name": "Đậu phụ sốt cà chua",
                "desc": "Đậu phụ sốt cà chua mềm mịn om cùng sốt cà chua đỏ tươi đậm đà, thơm mùi hành lá. Thời gian 15–30 phút, chi phí dưới 30.000 đồng."
            },
            "K22": {
                "name": "Miến xào rau củ",
                "desc": "Miến xào rau củ với những sợi miến dai mềm hòa quyện cùng rau củ tươi giòn (cà rốt, bắp cải, nấm) và gia vị đậm đà không bị nhão. Thời gian 15–30 phút, chi phí dưới 30.000 đồng."
            },
            "K23": {
                "name": "Khoai lang luộc",
                "desc": "Khoai lang luộc dân dã, ngọt dịu tự nhiên, mềm bở thơm ngon, ít dầu mỡ tốt cho tiêu hóa. Thời gian 15–30 phút, chi phí dưới 30.000 đồng."
            },
            "K24": {
                "name": "Sữa chua yến mạch và trái cây",
                "desc": "Món ăn nhẹ tươi mát kết hợp vị chua dịu của sữa chua, độ bùi mềm của yến mạch và vị ngọt từ trái cây tươi cắt nhỏ. Thời gian chuẩn bị dưới 15 phút, chi phí dưới 30.000 đồng."
            },
            "K25": {
                "name": "Salad ức gà",
                "desc": "Salad ức gà giàu dinh dưỡng kết hợp thịt gà áp chảo/luộc thái lát với xà lách, cà chua bi, dưa leo và sốt dầu ô liu chanh mật ong chua ngọt thanh nhẹ. Thời gian 15–30 phút, chi phí 30.000–50.000 đồng."
            },
            "K26": {
                "name": "Mì cay trộn hải sản",
                "desc": "Mì cay trộn hải sản sợi dai mềm trộn sốt cay đậm đà cùng tôm, mực, chả cá và rau củ tươi ngon. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K27": {
                "name": "Cá viên chiên sốt sa tế",
                "desc": "Cá viên chiên vàng giòn bên ngoài, dai mềm bên trong, phủ đều sốt sa tế cay nồng đậm đà kích thích vị giác. Thời gian 15–30 phút, chi phí 30.000–50.000 đồng."
            },
            "K28": {
                "name": "Bạch tuộc nướng muối ớt",
                "desc": "Bạch tuộc tươi nướng muối ớt cay nồng, giòn sần sật, thơm lừng mùi than hồng. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K29": {
                "name": "Cà tím nướng mỡ hành",
                "desc": "Cà tím nướng mềm nhuyễn ngọt tự nhiên, rưới mỡ hành xanh mướt béo ngậy và đậu phộng rang giã nhỏ. Thời gian 15–30 phút, chi phí dưới 30.000 đồng."
            },
            "K30": {
                "name": "Tôm nướng bơ tỏi",
                "desc": "Tôm tươi nướng chín săn chắc, thấm đẫm vị béo của bơ và hương thơm nồng nàn của tỏi phi. Thời gian 15–30 phút, chi phí trên 50.000 đồng."
            },
            "K31": {
                "name": "Thịt xiên nướng rau củ",
                "desc": "Thịt xiên nướng rau củ gồm thịt mềm mọng ướp gia vị xiên xen kẽ ớt chuông, hành tây, cà chua bi rồi nướng xém cạnh thơm phức. Thời gian trên 30 phút, chi phí trên 50.000 đồng."
            },
            "K32": {
                "name": "Khoai lang nướng mật ong",
                "desc": "Khoai lang nướng chín mềm bở tơi, phết lớp mật ong óng ánh tạo vị ngọt dịu và hương thơm hấp dẫn. Thời gian trên 30 phút, chi phí dưới 30.000 đồng."
            },
            "K33": {
                "name": "Canh bí đỏ nấu tôm",
                "desc": "Canh bí đỏ nấu tôm thanh nhẹ với vị ngọt mềm bùi của bí đỏ kết hợp vị ngọt đậm đà của tôm tươi, giàu dinh dưỡng. Thời gian 15–30 phút, chi phí 30.000–50.000 đồng."
            },
            "K34": {
                "name": "Bánh cuốn nhân thịt",
                "desc": "Bánh cuốn nhân thịt truyền thống với lớp bánh mỏng mềm mịn bao bọc nhân thịt heo mộc nhĩ xào thơm, ăn kèm chả lụa và nước mắm chua ngọt. Thời gian trên 30 phút, chi phí 30.000–50.000 đồng."
            },
            "K35": {
                "name": "Bánh canh cua",
                "desc": "Bánh canh cua thơm ngon với sợi bánh canh mềm dai, thịt cua tươi ngọt và nước dùng sánh nhẹ đậm đà đặc trưng từ hải sản. Thời gian trên 30 phút, chi phí trên 50.000 đồng."
            }
        }

        # 2. Tập luật suy diễn (Rule Base)
        self.rules = [
            # Cháo thịt bằm (K1)
            ({"T1", "L1", "N1", "V5", "G3", "D4"}, "K1"),
            ({"T1", "L1", "N1", "V5", "G3", "D3"}, "K1"),
            ({"T1", "L1", "N1", "V5", "G3", "D7"}, "K1"),
            ({"T1", "L1", "N1", "V5", "G3", "D8"}, "K1"),
            ({"T2", "L1", "N1", "V5", "G3", "D4"}, "K1"),
            ({"T2", "L1", "N1", "V5", "G3", "D3"}, "K1"),
            ({"T2", "L1", "N1", "V5", "G3", "D7"}, "K1"),
            ({"T2", "L1", "N1", "V5", "G3", "D8"}, "K1"),
            
            # Phở gà (K2)
            ({"T1", "L1", "N2", "V5", "G3", "D1"}, "K2"),
            ({"T1", "L1", "N2", "V5", "G3", "D3"}, "K2"),
            ({"T1", "L1", "N2", "V5", "G3", "D7"}, "K2"),
            ({"T1", "L1", "N2", "V5", "G3", "D8"}, "K2"),
            ({"T1", "L1", "N2", "V3", "G3", "D3"}, "K2"),
            ({"T1", "L1", "N2", "V3", "G3", "D7"}, "K2"),
            ({"T1", "L1", "N2", "V3", "G3", "D8"}, "K2"),
            ({"T2", "L1", "N2", "V5", "G3", "D1"}, "K2"),
            ({"T2", "L1", "N2", "V5", "G3", "D3"}, "K2"),
            ({"T2", "L1", "N2", "V5", "G3", "D7"}, "K2"),
            ({"T2", "L1", "N2", "V5", "G3", "D8"}, "K2"),
            ({"T2", "L1", "N2", "V3", "G3", "D7"}, "K2"),
            ({"T2", "L1", "N2", "V3", "G3", "D8"}, "K2"),

            # Bún riêu cua (K3)
            ({"T1", "L1", "N2", "V2", "G3", "D1"}, "K3"),
            ({"T1", "L1", "N2", "V2", "G3", "D2"}, "K3"),
            ({"T1", "L1", "N2", "V2", "G3", "D3"}, "K3"),
            ({"T1", "L1", "N2", "V3", "G3", "D2"}, "K3"),
            ({"T2", "L1", "N2", "V2", "G3", "D1"}, "K3"),
            ({"T2", "L1", "N2", "V2", "G3", "D3"}, "K3"),
            ({"T2", "L1", "N2", "V3", "G3", "D1"}, "K3"),
            ({"T2", "L1", "N2", "V3", "G3", "D2"}, "K3"),

            # Bún bò Huế (K4)
            ({"T1", "L1", "N2", "V3", "G3", "D1"}, "K4"),
            ({"T1", "L1", "N2", "V3", "G3", "D6"}, "K4"),
            ({"T1", "L1", "N2", "V1", "G3", "D1"}, "K4"),
            ({"T1", "L1", "N2", "V1", "G3", "D3"}, "K4"),
            ({"T1", "L1", "N2", "V1", "G3", "D6"}, "K4"),
            ({"T2", "L1", "N2", "V3", "G3", "D6"}, "K4"),
            ({"T2", "L1", "N2", "V1", "G3", "D1"}, "K4"),
            ({"T2", "L1", "N2", "V1", "G3", "D3"}, "K4"),
            ({"T2", "L1", "N2", "V1", "G3", "D6"}, "K4"),

            # Canh chua cá diêu hồng (K5)
            ({"T2", "L1", "N2", "V2", "G3", "D2"}, "K5"),
            ({"T3", "L1", "N2", "V2", "G3", "D1"}, "K5"),
            ({"T3", "L1", "N2", "V2", "G3", "D3"}, "K5"),
            ({"T3", "L1", "N2", "V2", "G3", "D2"}, "K5"),
            ({"T2", "L1", "N2", "V3", "G3", "D3"}, "K5"),
            ({"T3", "L1", "N2", "V3", "G3", "D1"}, "K5"),
            ({"T3", "L1", "N2", "V3", "G3", "D3"}, "K5"),
            ({"T3", "L1", "N2", "V3", "G3", "D2"}, "K5"),

            # Cơm chiên trứng (K6)
            ({"T1", "L2", "N1", "V3", "G1", "D1"}, "K6"),
            ({"T2", "L2", "N1", "V3", "G1", "D1"}, "K6"),
            ({"T3", "L2", "N1", "V3", "G1", "D1"}, "K6"),

            # Cơm rang dưa bò (K7)
            ({"T1", "L2", "N2", "V3", "G2", "D1"}, "K7"),
            ({"T1", "L2", "N2", "V3", "G2", "D3"}, "K7"),
            ({"T1", "L2", "N2", "V3", "G2", "D6"}, "K7"),
            ({"T1", "L2", "N2", "V2", "G2", "D1"}, "K7"),
            ({"T1", "L2", "N2", "V2", "G2", "D3"}, "K7"),
            ({"T1", "L2", "N2", "V2", "G2", "D6"}, "K7"),
            ({"T2", "L2", "N2", "V3", "G2", "D1"}, "K7"),
            ({"T2", "L2", "N2", "V3", "G2", "D3"}, "K7"),
            ({"T2", "L2", "N2", "V3", "G2", "D6"}, "K7"),
            ({"T2", "L2", "N2", "V2", "G2", "D6"}, "K7"),
            ({"T3", "L2", "N2", "V3", "G2", "D1"}, "K7"),
            ({"T3", "L2", "N2", "V3", "G2", "D3"}, "K7"),
            ({"T3", "L2", "N2", "V3", "G2", "D6"}, "K7"),
            ({"T3", "L2", "N2", "V2", "G2", "D6"}, "K7"),

            # Cơm sườn nướng (K8)
            ({"T2", "L2", "N2", "V4", "G3", "D3"}, "K8"),
            ({"T2", "L2", "N2", "V4", "G3", "D1"}, "K8"),
            ({"T2", "L2", "N2", "V3", "G3", "D3"}, "K8"),
            ({"T3", "L2", "N2", "V4", "G3", "D3"}, "K8"),
            ({"T3", "L2", "N2", "V4", "G3", "D1"}, "K8"),
            ({"T3", "L2", "N2", "V3", "G3", "D3"}, "K8"),
            ({"T3", "L2", "N2", "V3", "G3", "D1"}, "K8"),

            # Bún thịt nướng (K9)
            ({"T1", "L2", "N2", "V3", "G3", "D1"}, "K9"),
            ({"T1", "L2", "N2", "V3", "G3", "D3"}, "K9"),
            ({"T1", "L2", "N2", "V3", "G3", "D2"}, "K9"),
            ({"T1", "L2", "N2", "V2", "G3", "D1"}, "K9"),
            ({"T1", "L2", "N2", "V2", "G3", "D3"}, "K9"),
            ({"T1", "L2", "N2", "V2", "G3", "D2"}, "K9"),
            ({"T2", "L2", "N2", "V3", "G3", "D1"}, "K9"),
            ({"T2", "L2", "N2", "V3", "G3", "D2"}, "K9"),
            ({"T2", "L2", "N2", "V2", "G3", "D1"}, "K9"),
            ({"T2", "L2", "N2", "V2", "G3", "D3"}, "K9"),
            ({"T2", "L2", "N2", "V2", "G3", "D2"}, "K9"),

            # Cá sốt cà chua (K10)
            ({"T2", "L2", "N2", "V2", "G2", "D1"}, "K10"),
            ({"T2", "L2", "N2", "V1", "G2", "D1"}, "K10"),
            ({"T3", "L2", "N2", "V2", "G2", "D1"}, "K10"),
            ({"T3", "L2", "N2", "V1", "G2", "D1"}, "K10"),

            # Gỏi gà rau củ (K11)
            ({"T2", "L2", "N3", "V2", "G2", "D1"}, "K11"),
            ({"T2", "L2", "N3", "V2", "G2", "D2"}, "K11"),
            ({"T2", "L2", "N3", "V2", "G2", "D3"}, "K11"),
            ({"T2", "L2", "N3", "V2", "G2", "D5"}, "K11"),
            ({"T2", "L2", "N3", "V5", "G2", "D1"}, "K11"),
            ({"T2", "L2", "N3", "V5", "G2", "D2"}, "K11"),
            ({"T2", "L2", "N3", "V5", "G2", "D3"}, "K11"),
            ({"T2", "L2", "N3", "V5", "G2", "D5"}, "K11"),
            ({"T3", "L2", "N3", "V2", "G2", "D1"}, "K11"),
            ({"T3", "L2", "N3", "V2", "G2", "D2"}, "K11"),
            ({"T3", "L2", "N3", "V2", "G2", "D3"}, "K11"),
            ({"T3", "L2", "N3", "V2", "G2", "D5"}, "K11"),
            ({"T3", "L2", "N3", "V5", "G2", "D1"}, "K11"),
            ({"T3", "L2", "N3", "V5", "G2", "D2"}, "K11"),
            ({"T3", "L2", "N3", "V5", "G2", "D3"}, "K11"),
            ({"T3", "L2", "N3", "V5", "G2", "D5"}, "K11"),

            # Cá diêu hồng chiên xù (K12)
            ({"T2", "L3", "N3", "V3", "G2", "D1"}, "K12"),
            ({"T2", "L3", "N3", "V3", "G2", "D3"}, "K12"),
            ({"T3", "L3", "N3", "V3", "G2", "D1"}, "K12"),
            ({"T3", "L3", "N3", "V3", "G2", "D3"}, "K12"),

            # Cánh gà chiên nước mắm (K13)
            ({"T2", "L3", "N3", "V3", "G2", "D7"}, "K13"),
            ({"T2", "L3", "N3", "V4", "G2", "D3"}, "K13"),
            ({"T2", "L3", "N3", "V4", "G2", "D7"}, "K13"),
            ({"T3", "L3", "N3", "V3", "G2", "D7"}, "K13"),
            ({"T3", "L3", "N3", "V4", "G2", "D3"}, "K13"),
            ({"T3", "L3", "N3", "V4", "G2", "D7"}, "K13"),

            # Đậu phụ chiên sả ớt (K14)
            ({"T2", "L6", "N1", "V1", "G2", "D8"}, "K14"),
            ({"T2", "L6", "N1", "V3", "G2", "D8"}, "K14"),
            ({"T3", "L6", "N1", "V1", "G2", "D8"}, "K14"),
            ({"T3", "L6", "N1", "V3", "G2", "D8"}, "K14"),
            ({"T2", "L3", "N1", "V1", "G2", "D8"}, "K14"),
            ({"T2", "L3", "N1", "V3", "G2", "D8"}, "K14"),
            ({"T3", "L3", "N1", "V1", "G2", "D8"}, "K14"),
            ({"T3", "L3", "N1", "V3", "G2", "D8"}, "K14"),

            # Trứng chiên hành (K15)
            ({"T1", "L3", "N1", "V3", "G1", "D8"}, "K15"),
            ({"T1", "L3", "N1", "V3", "G1", "D3"}, "K15"),
            ({"T2", "L3", "N1", "V3", "G1", "D8"}, "K15"),
            ({"T2", "L3", "N1", "V3", "G1", "D3"}, "K15"),
            ({"T3", "L3", "N1", "V3", "G1", "D8"}, "K15"),
            ({"T3", "L3", "N1", "V3", "G1", "D3"}, "K15"),

            # Thịt ba chỉ luộc (K16)
            ({"T2", "L4", "N2", "V5", "G2", "D3"}, "K16"),
            ({"T3", "L4", "N2", "V5", "G2", "D3"}, "K16"),

            # Rau muống luộc (K17)
            ({"T2", "L4", "N1", "V5", "G1", "D2"}, "K17"),
            ({"T2", "L4", "N1", "V5", "G1", "D8"}, "K17"),
            ({"T3", "L4", "N1", "V5", "G1", "D2"}, "K17"),
            ({"T3", "L4", "N1", "V5", "G1", "D8"}, "K17"),
            ({"T2", "L6", "N1", "V5", "G1", "D2"}, "K17"),
            ({"T2", "L6", "N1", "V5", "G1", "D5"}, "K17"),
            ({"T2", "L6", "N1", "V5", "G1", "D8"}, "K17"),
            ({"T3", "L6", "N1", "V5", "G1", "D2"}, "K17"),
            ({"T3", "L6", "N1", "V5", "G1", "D5"}, "K17"),
            ({"T3", "L6", "N1", "V5", "G1", "D8"}, "K17"),

            # Rau củ luộc (K18)
            ({"T2", "L4", "N1", "V5", "G2", "D2"}, "K18"),
            ({"T2", "L4", "N1", "V5", "G2", "D5"}, "K18"),
            ({"T2", "L4", "N1", "V5", "G2", "D8"}, "K18"),
            ({"T3", "L4", "N1", "V5", "G2", "D2"}, "K18"),
            ({"T3", "L4", "N1", "V5", "G2", "D8"}, "K18"),
            ({"T2", "L6", "N1", "V5", "G2", "D2"}, "K18"),
            ({"T2", "L6", "N1", "V5", "G2", "D5"}, "K18"),
            ({"T2", "L6", "N1", "V5", "G2", "D8"}, "K18"),
            ({"T3", "L6", "N1", "V5", "G2", "D2"}, "K18"),
            ({"T3", "L6", "N1", "V5", "G2", "D8"}, "K18"),

            # Trứng luộc (K19)
            ({"T1", "L4", "N1", "V5", "G1", "D5"}, "K19"),
            ({"T1", "L4", "N1", "V5", "G1", "D3"}, "K19"),
            ({"T1", "L4", "N1", "V5", "G1", "D6"}, "K19"),
            ({"T1", "L4", "N1", "V5", "G1", "D7"}, "K19"),
            ({"T1", "L4", "N1", "V5", "G1", "D4"}, "K19"),
            ({"T2", "L4", "N1", "V5", "G1", "D5"}, "K19"),
            ({"T2", "L4", "N1", "V5", "G1", "D3"}, "K19"),
            ({"T2", "L4", "N1", "V5", "G1", "D6"}, "K19"),
            ({"T2", "L4", "N1", "V5", "G1", "D7"}, "K19"),
            ({"T2", "L4", "N1", "V5", "G1", "D4"}, "K19"),
            ({"T3", "L4", "N1", "V5", "G1", "D5"}, "K19"),
            ({"T3", "L4", "N1", "V5", "G1", "D3"}, "K19"),
            ({"T3", "L4", "N1", "V5", "G1", "D6"}, "K19"),
            ({"T3", "L4", "N1", "V5", "G1", "D7"}, "K19"),
            ({"T3", "L4", "N1", "V5", "G1", "D4"}, "K19"),

            # Gà luộc (K20)
            ({"T2", "L4", "N3", "V5", "G3", "D3"}, "K20"),
            ({"T2", "L4", "N3", "V5", "G3", "D6"}, "K20"),
            ({"T3", "L4", "N3", "V5", "G3", "D3"}, "K20"),
            ({"T3", "L4", "N3", "V5", "G3", "D6"}, "K20"),

            # Đậu phụ sốt cà chua (K21)
            ({"T2", "L2", "N1", "V2", "G2", "D8"}, "K21"),
            ({"T2", "L2", "N1", "V2", "G2", "D1"}, "K21"),
            ({"T3", "L2", "N1", "V2", "G2", "D8"}, "K21"),
            ({"T3", "L2", "N1", "V2", "G2", "D1"}, "K21"),

            # Miến xào rau củ (K22)
            ({"T1", "L2", "N1", "V3", "G2", "D2"}, "K22"),
            ({"T2", "L2", "N1", "V3", "G2", "D2"}, "K22"),
            ({"T3", "L2", "N1", "V3", "G2", "D2"}, "K22"),
            ({"T1", "L6", "N1", "V3", "G2", "D2"}, "K22"),
            ({"T2", "L6", "N1", "V3", "G2", "D2"}, "K22"),

            # Khoai lang luộc (K23)
            ({"T1", "L4", "N1", "V5", "G2", "D4"}, "K23"),
            ({"T1", "L4", "N1", "V5", "G2", "D5"}, "K23"),
            ({"T3", "L4", "N1", "V5", "G2", "D4"}, "K23"),
            ({"T3", "L4", "N1", "V5", "G2", "D5"}, "K23"),
            ({"T1", "L6", "N1", "V5", "G2", "D5"}, "K23"),
            ({"T3", "L6", "N1", "V5", "G2", "D4"}, "K23"),
            ({"T3", "L6", "N1", "V5", "G2", "D5"}, "K23"),

            # Sữa chua yến mạch và trái cây (K24)
            ({"T1", "L6", "N1", "V2", "G2", "D4"}, "K24"),
            ({"T1", "L2", "N1", "V2", "G2", "D4"}, "K24"),
            ({"T1", "L2", "N1", "V2", "G2", "D6"}, "K24"),
            ({"T1", "L2", "N1", "V2", "G2", "D7"}, "K24"),
            ({"T1", "L2", "N1", "V2", "G2", "D8"}, "K24"),
            ({"T1", "L2", "N1", "V2", "G2", "D5"}, "K24"),
            ({"T3", "L2", "N1", "V2", "G2", "D4"}, "K24"),
            ({"T3", "L2", "N1", "V2", "G2", "D6"}, "K24"),
            ({"T3", "L2", "N1", "V2", "G2", "D7"}, "K24"),
            ({"T3", "L2", "N1", "V2", "G2", "D5"}, "K24"),

            # Salad ức gà (K25)
            ({"T2", "L2", "N2", "V2", "G2", "D5"}, "K25"),
            ({"T2", "L2", "N2", "V2", "G2", "D3"}, "K25"),
            ({"T2", "L2", "N2", "V2", "G2", "D2"}, "K25"),
            ({"T3", "L2", "N2", "V2", "G2", "D5"}, "K25"),
            ({"T3", "L2", "N2", "V2", "G2", "D3"}, "K25"),
            ({"T3", "L2", "N2", "V2", "G2", "D2"}, "K25"),

            # Mì cay trộn hải sản (K26)
            ({"T2", "L2", "N3", "V1", "G2", "D2"}, "K26"),
            ({"T2", "L2", "N3", "V1", "G2", "D3"}, "K26"),
            ({"T3", "L2", "N3", "V1", "G2", "D2"}, "K26"),
            ({"T3", "L2", "N3", "V1", "G2", "D3"}, "K26"),
            ({"T2", "L2", "N3", "V3", "G2", "D2"}, "K26"),
            ({"T2", "L2", "N3", "V3", "G2", "D3"}, "K26"),
            ({"T3", "L2", "N3", "V3", "G2", "D2"}, "K26"),
            ({"T3", "L2", "N3", "V3", "G2", "D3"}, "K26"),

            # Cá viên chiên sốt sa tế (K27)
            ({"T3", "L3", "N2", "V1", "G2", "D4"}, "K27"),
            ({"T3", "L3", "N2", "V3", "G2", "D4"}, "K27"),

            # Bạch tuộc nướng muối ớt (K28)
            ({"T3", "L5", "N3", "V1", "G2", "D3"}, "K28"),
            ({"T3", "L5", "N3", "V4", "G2", "D3"}, "K28"),
            ({"T2", "L5", "N3", "V1", "G2", "D3"}, "K28"),
            ({"T2", "L5", "N3", "V4", "G2", "D3"}, "K28"),

            # Cà tím nướng mỡ hành (K29)
            ({"T2", "L5", "N1", "V3", "G2", "D2"}, "K29"),
            ({"T3", "L5", "N1", "V3", "G2", "D2"}, "K29"),
            ({"T3", "L6", "N1", "V3", "G2", "D2"}, "K29"),

            # Tôm nướng bơ tỏi (K30)
            ({"T2", "L5", "N3", "V3", "G2", "D3"}, "K30"),
            ({"T3", "L5", "N3", "V3", "G2", "D3"}, "K30"),

            # Thịt xiên nướng rau củ (K31)
            ({"T2", "L5", "N3", "V3", "G3", "D3"}, "K31"),
            ({"T2", "L5", "N3", "V3", "G3", "D1"}, "K31"),
            ({"T2", "L5", "N3", "V3", "G3", "D2"}, "K31"),
            ({"T2", "L5", "N3", "V4", "G3", "D3"}, "K31"),
            ({"T2", "L5", "N3", "V4", "G3", "D1"}, "K31"),
            ({"T2", "L5", "N3", "V4", "G3", "D2"}, "K31"),
            ({"T3", "L5", "N3", "V3", "G3", "D3"}, "K31"),
            ({"T3", "L5", "N3", "V3", "G3", "D1"}, "K31"),
            ({"T3", "L5", "N3", "V3", "G3", "D2"}, "K31"),
            ({"T3", "L5", "N3", "V4", "G3", "D3"}, "K31"),
            ({"T3", "L5", "N3", "V4", "G3", "D1"}, "K31"),
            ({"T3", "L5", "N3", "V4", "G3", "D2"}, "K31"),

            # Khoai lang nướng mật ong (K32)
            ({"T1", "L5", "N1", "V5", "G3", "D4"}, "K32"),
            ({"T1", "L5", "N1", "V5", "G3", "D5"}, "K32"),
            ({"T3", "L5", "N1", "V5", "G3", "D4"}, "K32"),
            ({"T3", "L5", "N1", "V5", "G3", "D5"}, "K32"),
            ({"T1", "L6", "N1", "V5", "G3", "D4"}, "K32"),
            ({"T1", "L6", "N1", "V5", "G3", "D5"}, "K32"),
            ({"T3", "L6", "N1", "V5", "G3", "D4"}, "K32"),
            ({"T3", "L6", "N1", "V5", "G3", "D5"}, "K32"),

            # Canh bí đỏ nấu tôm (K33)
            ({"T2", "L1", "N2", "V5", "G2", "D3"}, "K33"),
            ({"T3", "L1", "N2", "V5", "G2", "D3"}, "K33"),
            ({"T2", "L1", "N2", "V5", "G2", "D1"}, "K33"),
            ({"T3", "L1", "N2", "V5", "G2", "D1"}, "K33"),
            ({"T2", "L1", "N2", "V5", "G2", "D2"}, "K33"),

            # Bánh cuốn nhân thịt (K34)
            ({"T1", "L2", "N2", "V5", "G3", "D3"}, "K34"),
            ({"T3", "L2", "N2", "V5", "G3", "D3"}, "K34"),

            # Bánh canh cua (K35)
            ({"T2", "L1", "N3", "V3", "G3", "D1"}, "K35"),
            ({"T3", "L1", "N3", "V3", "G3", "D1"}, "K35"),
            ({"T1", "L1", "N3", "V3", "G3", "D1"}, "K35"),
            ({"T2", "L1", "N3", "V3", "G3", "D3"}, "K35"),
            ({"T3", "L1", "N3", "V3", "G3", "D3"}, "K35"),
            ({"T1", "L1", "N3", "V3", "G3", "D3"}, "K35"),
        ]

        # Tự động quét file ảnh tương ứng
        self.dish_images = {}
        for i, code in enumerate(self.dishes.keys(), 1):
            found_img = ""
            for ext in [".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"]:
                possible_names = [f"K{i}{ext}", f"image{i}{ext}", f"{i}{ext}"]
                for name in possible_names:
                    if os.path.exists(name):
                        found_img = name
                        break
                if found_img:
                    break
            self.dish_images[code] = found_img

    def inference(self, user_facts):
        matched_dishes = set()
        user_facts_set = set(user_facts)
        
        for conditions, conclusion in self.rules:
            if conditions.issubset(user_facts_set):
                matched_dishes.add(conclusion)
                
        result = []
        for code in matched_dishes:
            if code in self.dishes:
                result.append({
                    "code": code,
                    "name": self.dishes[code]["name"],
                    "desc": self.dishes[code]["desc"],
                    "image": self.dish_images.get(code, "")
                })
        return result

@st.cache_resource
def load_expert_system():
    return FoodExpertSystem()

system = load_expert_system()

# --- GIAO DIỆN WEB STREAMLIT ---
st.set_page_config(page_title="Hệ Thống Chuyên Gia Tư Vấn Món Ăn", page_icon="🍽️", layout="centered")

st.title("🍽️ Hệ Thống Chuyên Gia Tư Vấn Món Ăn")
st.write("Vui lòng chọn các tiêu chí của bạn dưới đây để hệ thống gợi ý món ăn phù hợp:")

# Giao diện chọn tiêu chí
time_option = st.selectbox(
    "1. Thời điểm ăn:",
    options=["T1", "T2", "T3"],
    format_func=lambda x: {"T1": "T1: Sáng", "T2": "T2: Trưa", "T3": "T3: Tối"}[x]
)

type_option = st.selectbox(
    "2. Loại món ăn ưa thích:",
    options=["L1", "L2", "L3", "L4", "L5", "L6"],
    format_func=lambda x: {
        "L1": "L1: Món nước", "L2": "L2: Món khô", "L3": "L3: Món rán", 
        "L4": "L4: Món luộc", "L5": "L5: Món nướng", "L6": "L6: Món chay"
    }[x]
)

budget_option = st.selectbox(
    "3. Ngân sách:",
    options=["N1", "N2", "N3"],
    format_func=lambda x: {
        "N1": "N1: Dưới 30.000đ", "N2": "N2: Từ 30.000đ đến 50.000đ", "N3": "N3: Trên 50.000đ"
    }[x]
)

taste_option = st.selectbox(
    "4. Khẩu vị:",
    options=["V1", "V2", "V3", "V4", "V5"],
    format_func=lambda x: {
        "V1": "V1: Cay", "V2": "V2: Chua ngọt", "V3": "V3: Đậm đà", 
        "V4": "V4: Mặn mà", "V5": "V5: Thanh nhẹ"
    }[x]
)

prep_option = st.selectbox(
    "5. Thời gian chuẩn bị:",
    options=["G1", "G2", "G3"],
    format_func=lambda x: {
        "G1": "G1: Dưới 15 phút", "G2": "G2: Từ 15 đến 30 phút", "G3": "G3: Trên 30 phút"
    }[x]
)

nutrition_option = st.selectbox(
    "6. Nhu cầu dinh dưỡng:",
    options=["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"],
    format_func=lambda x: {
        "D1": "D1: Đủ chất", "D2": "D2: Nhiều rau", "D3": "D3: Giàu đạm", 
        "D4": "D4: Ăn nhẹ", "D5": "D5: Giảm cân", "D6": "D6: Thể thao", 
        "D7": "D7: Dành cho trẻ em", "D8": "D8: Dành cho người già"
    }[x]
)

# Nút bấm tìm kiếm
if st.button("🔍 Tìm Món Ăn Phù Hợp", type="primary"):
    user_facts = [time_option, type_option, budget_option, taste_option, prep_option, nutrition_option]
    
    recommendations = system.inference(user_facts)
    
    st.markdown("---")
    st.subheader("✨ Kết quả gợi ý từ hệ thống chuyên gia:")
    
    if recommendations:
        for item in recommendations:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    if item["image"] and os.path.exists(item["image"]):
                        st.image(item["image"], caption=item["name"], use_container_width=True)
                    else:
                        st.info("Chưa có hình ảnh minh họa")
                with col2:
                    st.success(f"**Món ăn:** {item['name']} (`{item['code']}`)")
                    st.write(f"**Mô tả:** {item['desc']}")
                    st.caption("Khớp hoàn hảo với các tiêu chí bạn đã chọn!")
                st.markdown("---")
    else:
        st.error("Rất tiếc, hệ thống không tìm thấy món ăn nào khớp chính xác với tập tiêu chí này. Hãy thử thay đổi một vài lựa chọn nhé!")