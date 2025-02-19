from scripts.server import URSocket
from scripts.robot import init_robot
import time

class URController:

    

    def __init__(self):
        self.sock = URSocket(debug=True)
        init_robot(self.sock)

        self.Moveaway_from_p="p[.376623774417, -.070910473746, .001801155367, -.378306456663, 3.112454516703, .012986017208]"
        self.Moveaway_to_p="p[.376439639169, -.071235459681, .036914627345, -.378240332221, 3.112467796797, .012920658447]"
        self.Reset_p="p[.283658307565, -.347660256071, .424117552911, .694819419243, 1.754722016139, -1.538816710004]"
        self.Reset_q="[-3.799697462712423, -1.3525857639363785, 1.7859233061419886, 2.783622904414795, -2.3332553545581263, 0.9564146995544434]"
        self.High1_p="p[.383923892194, -.436794366941, .355882691833, .770866103048, 1.921460503539, -1.517501335387]"
        self.High1_q="[-3.792715851460592, -0.8057329219630738, 1.0584147612201136, 3.1758362489887695, -2.389451328908102, 1.0564604997634888]"
        self.Setdown_from_p="p[.383929597290, -.436805314879, .355860543316, .770835509037, 1.921534132609, -1.517522683519]"
        self.Setdown_to_p="p[.379546938541, -.439674711440, .329517075152, .706496493548, 1.795959030748, -1.636075283020]"
        self.Setup_from_p="p[.384068117791, -.436577644833, .330268594615, .770834468257, 1.921491104357, -1.517474595650]"
        self.Setup_to_p="p[.383914886555, -.436801558250, .355875511369, .770902716690, 1.921431775437, -1.517494341675]"
        self.High2_p="p[.346608810219, -.435527949910, .355667318972, .770792286172, 1.921501972866, -1.517392957842]"
        self.High2_q="[-3.8518269697772425, -0.9572653335383912, 1.3284443060504358, 3.0409957605549316, -2.332668129597799, 1.0333276987075806]"
        self.High3_p="p[.310654891907, -.434331639067, .355520000167, .770847328453, 1.921463503686, -1.517476065221]"
        self.High3_q="[-3.9200268427478235, -1.0886546236327668, 1.547826115285055, 2.937222643489502, -2.266984764729635, 1.0095351934432983]"
        self.High4_p="p[.275219049685, -.433139676498, .355386575131, .770826198448, 1.921414544468, -1.517515018134]"
        self.High4_q="[-4.001431767140524, -1.2128001016429444, 1.7400792280780237, 2.8538028436848144, -2.1881230513202112, 0.9843456149101257]"
        self.High5_p="p[.243746934823, -.432073987441, .355242743949, .770766198360, 1.921415778873, -1.517508684155]"
        self.High5_q="[-4.089252297078268, -1.3229243171266098, 1.896421257649557, 2.7945615488239746, -2.102672878895895, 0.9601733684539795]"
        self.High6_p="p[.208102189615, -.430909972941, .355053536542, .770871303736, 1.921426933467, -1.517550577333]"
        self.High6_q="[-4.2122536341296595, -1.451815740471222, 2.060046974812643, 2.746354265803955, -1.9827335516559046, 0.9301550984382629]"
        self.High7_p="p[.171431770689, -.429665739503, .354906115589, .770830549235, 1.921357967341, -1.517565443450]"
        self.High7_q="[-4.374709073697225, -1.595964094201559, 2.2156737486468714, 2.723489924068115, -1.8237112204181116, 0.8948841094970703]"
        self.Plinko_Reset_p="p[.297690553083, -.194046922432, .645481875831, .386368595433, 1.840559467859, -.867299053253]"
        self.Plinko_Reset_q="[-3.8191383520709437, -1.7399875126280726, 0.620101277028219, 4.48345057546582, -1.7113006750689905, 1.1948678493499756]"
        self.Plinko_Point1_p="p[.618627993801, -.119006959169, .627974502819, -.624325456845, 1.489125426322, -.586010917470]"
        self.Plinko_Point1_q="[-3.8085432688342493, -0.8505228322795411, 0.060010735188619435, 3.9462825494953613, -0.8845532576190394, 0.7880352735519409]"
        self.Plinko_Point_2_p="p[.618674112853, -.118864168449, .612340260274, -.624300112788, 1.489056706322, -.586049952122]"
        self.Plinko_Point_2_q="[-3.8077579180346888, -0.5876795810512085, -0.4522317051887512, 4.195774717921875, -0.8848875204669397, 0.7877804040908813]"

        self.board_points = [self.High1_p, self.High2_p, self.High3_p, self.High4_p, self.High5_p, self.High6_p, self.High7_p]
        self.board_poses = [self.High1_q, self.High2_q, self.High3_q, self.High4_q, self.High5_q, self.High6_q, self.High7_q]

    def drop_in_column(self, column_number):
        point = self.board_points[column_number - 1]
        pose = self.board_points[column_number - 1]

        #Go to point above the correct column
        self.sock.send_cmd(f'movej(get_inverse_kin({point}, qnear={pose}), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        #Go down into the slot
        self.sock.send_cmd(f'movej(pose_add(get_target_tcp_pose(), pose_sub({self.Setdown_to_p}, {self.Setdown_from_p})), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

        #Drop the piece
        self.sock.send_cmd('set_standard_digital_out(1, False)')
        self.sock.send_cmd('set_standard_digital_out(5, False)')
        time.sleep(1) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movej(get_inverse_kin({point}, qnear={pose}), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

    # JM W pick up from point on collection plate
    def pick_up_from_plate(self, point):

        #Go to point above the correct column
        self.sock.send_cmd(f'movej(get_inverse_kin({point}, qnear={pose}), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        #Go down into the slot
        self.sock.send_cmd(f'movej(pose_add(get_target_tcp_pose(), pose_sub({self.Setdown_to_p}, {self.Setdown_from_p})), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

        #Drop the piece
        self.sock.send_cmd('set_standard_digital_out(1, False)')
        self.sock.send_cmd('set_standard_digital_out(5, False)')
        time.sleep(1) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movej(get_inverse_kin({point}, qnear={pose}), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time


