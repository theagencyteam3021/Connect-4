from scripts.server import URSocket
from scripts.robot import init_robot
import time

class URController:

    

    def __init__(self):
        self.sock = URSocket(debug=True)
        init_robot(self.sock)
        self.Uppiece_p='p[.054423610889, -.259093589869, .499907872505, .984026369311, 1.904306948412, -1.690607669317]'
        self.Uppiece_q='[-4.799920980130331, -2.648378988305563, 1.9133709112750452, 4.05726067602124, -1.6337721983539026, 0.8141733407974243]'
        self.PickUp_from_p='p[.375739482937, -.086634922480, .042262099523, -.378230322671, 3.112559633039, .013042208682]'
        self.PickUp_to_p='p[.377848073688, -.085419996674, .022825539051, -.378246720523, 3.112584990394, .013056245636]'
        self.Moveaway_from_p='p[.386130121457, -.086636404499, .021374953430, -.378130646312, 3.112636447661, .013028787136]'
        self.Moveaway_to_p='p[.386134135970, -.086627753675, .045107121874, -.378222226500, 3.112584802764, .013036704789]'
        self.Reset_p='p[.283658307565, -.347660256071, .424117552911, .694819419243, 1.754722016139, -1.538816710004]'
        self.Reset_q='[-3.799697462712423, -1.3525857639363785, 1.7859233061419886, 2.783622904414795, -2.3332553545581263, 0.9564146995544434]'
        self.High1_p='p[.367877667881, -.423732481931, .395600183424, .829503325153, 1.765644513379, -1.717871675727]'
        self.High1_q='[-3.752244536076681, -0.6144036215594788, 0.740582291279928, 3.0938936907001953, -2.5727646986590784, 0.9027394652366638]'
        self.Low1_p='p[.367900771377, -.423721925314, .339865060794, .829441287257, 1.765663795440, -1.717833269055]'
        self.Low1_q='[-3.7522154490100306, -0.54299350202594, 0.8676307837115687, 2.894875689143799, -2.5728874842273157, 0.9020636677742004]'
        self.Setup_from_p='p[.368185691159, -.420565915416, .338487130527, .758018932415, 1.773693887809, -1.672339406733]'
        self.Setup_to_p='p[.368176896763, -.420584486545, .387693022958, .758060061407, 1.773696302070, -1.672376836552]'
        self.High2_p='p[.332282880016, -.423748739315, .395585541109, .829519489841, 1.765644042464, -1.717847316381]'
        self.High2_q='[-3.8052521387683313, -0.792907790546753, 1.0780742804156702, 2.9289871889301757, -2.520080629979269, 0.8955117464065552]'
        self.Low2_p='p[.332267809939, -.423737582847, .337681707244, .829554692532, 1.765608029301, -1.717873199044]'
        self.Low2_q='[-3.805220429097311, -0.6933992070010682, 1.1818807760821741, 2.7250534731098632, -2.520257536564962, 0.8947821855545044]'
        self.High3_p='p[.297759137872, -.422120673359, .391207278905, .829538861696, 1.765579569738, -1.717829700630]'
        self.High3_q='[-3.862243715916769, -0.9289674919894715, 1.3440101782428187, 2.793801947230957, -2.4633188883410853, 0.8888114094734192]'
        self.Low3_p='p[.297758607334, -.422114432863, .338763234527, .829501862162, 1.765588253689, -1.717865574557]'
        self.Low3_q='[-3.8621955553637903, -0.8214973372272034, 1.4287927786456507, 2.6010004717060546, -2.463442866002218, 0.8880841135978699]'
        self.High4_p='p[.262647025743, -.420583851387, .389502026751, .829547110731, 1.765565994887, -1.717845899011]'
        self.High4_q='[-3.931977097188131, -1.0562655490687867, 1.5692461172686976, 2.6906911569782714, -2.3937881628619593, 0.8818391561508179]'
        self.Low4_p='p[.262656288517, -.420574697985, .336940905228, .829537223778, 1.765631658629, -1.717804446755]'
        self.Low4_q='[-3.931875530873434, -0.9311188024333497, 1.6510770956622522, 2.483290835017822, -2.3939242998706263, 0.8811960816383362]'
        self.High5_p='p[.226994023810, -.420577191536, .377964320515, .829510921597, 1.765572275557, -1.717830319530]'
        self.High5_q='[-4.022103134785787, -1.1526362162879487, 1.7892711798297327, 2.561782045955322, -2.3038185278521937, 0.8741377592086792]'
        self.Low5_p='p[.226991502482, -.420569261674, .338530858597, .829524596066, 1.765490138512, -1.717815690008]'
        self.Low5_q='[-4.022021595631735, -1.0420042437366028, 1.8486517111407679, 2.391364737147949, -2.3039143721209925, 0.8736402988433838]'
        self.High6_p='p[.191774147064, -.418866437127, .394332425826, .845232833621, 1.763899787555, -1.727433253824]'
        self.High6_q='[-4.114674631749288, -1.3016888958266755, 1.913853947316305, 2.583357496852539, -2.2266510168658655, 0.8689883947372437]'
        self.Low6_p='p[.191793810125, -.418857777775, .339129630572, .845150058479, 1.763779827951, -1.727376431985]'
        self.Low6_q='[-4.114522759114401, -1.1350270968726655, 2.010949436818258, 2.3190454679676513, -2.2267444769488733, 0.8682615756988525]'
        self.High7_p='p[.157819568982, -.417395667668, .383632905433, .837043144380, 1.743967239446, -1.741948049389]'
        self.High7_q='[-4.242265526448385, -1.3689162892154236, 2.1031225363360804, 2.4342095094868164, -2.0996692816363733, 0.8506059050559998]'
        self.Low7_p='p[.157868849393, -.417402298831, .337690163176, .836924210002, 1.744015275450, -1.741869509378]'
        self.Low7_q='[-4.242028299962179, -1.1989190441421052, 2.1792991797076624, 2.1877357202717285, -2.099783722554342, 0.8499569296836853]'
        self.Plinko_Reset_p='p[.344200881006, -.333937468008, .744468401573, .221533876087, 1.514098284181, -1.372686352557]'
        self.Plinko_Reset_q='[-4.076216046010153, -1.1923377376845856, 0.2538488546954554, 3.888868494624756, -1.6176698843585413, 0.8710737824440002]'
        self.Plinko_Point1_p='p[.595962463701, -.201904714105, .606146446172, -1.004933677079, 1.379785948807, -.995298248346]'
        self.Plinko_Point1_q='[-4.08470589319338, -0.8768575948527833, 0.2541125456439417, 3.827688379878662, -0.6530912558185022, 0.23826520144939423]'
        self.go_upw_from_p='p[.368490239414, -.420328009479, .338486155165, .757288994819, 1.773729175409, -1.671797031078]'
        self.go_upw_to_p='p[.368199803788, -.420566825158, .386457575354, .757977659301, 1.773784881344, -1.672349860401]'
        self.Setdown_from_p='p[.368189332974, -.420572372214, .386477734558, .757995392526, 1.773716570238, -1.672337576525]'
        self.Setdown_to_p='p[.367920499991, -.425368891837, .339617841601, .829391370564, 1.765682256350, -1.717820716283]'


        # incomplete: add relative movement to grab piece off plate
        self.Go_Down_To_Grab_p=[]

        self.board_points = [self.High1_p, self.High2_p, self.High3_p, self.High4_p, self.High5_p, self.High6_p, self.High7_p]
        self.board_poses = [self.High1_q, self.High2_q, self.High3_q, self.High4_q, self.High5_q, self.High6_q, self.High7_q]
        
        self.low_points = [self.Low1_p, self.Low2_p, self.Low3_p, self.Low4_p, self.Low5_p, self.Low6_p, self.Low7_p]

    def drop_in_column(self, column_number):
        point = self.board_points[column_number - 1]
        pose = self.board_points[column_number - 1]
        low_point = self.low_points[column_number - 1]

        #Go to point above the correct column
        self.sock.send_cmd(f'movej({point}, a=1.2, v=1.0471975511965976)')
        time.sleep(3) #TODO tune this time

        #Go down into the slot
        self.sock.send_cmd(f'movel({low_point}, a=1.2, v=0.25)')
        time.sleep(1) #TODO tune this time

        #Drop the piece
        self.sock.send_cmd('set_standard_digital_out(1, False)')
        #self.sock.send_cmd('set_standard_digital_out(5, False)')
        time.sleep(0.5) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movel({point}, a=1.2, v=0.25)')
        time.sleep(1) #TODO tune this time
        
    # JM W pick up from point on collection plate
    def pick_up_from_plate(self, point):

        #Go to point above the correct column
        self.sock.send_cmd(f'movej({point}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        #Go down to spot
        # pose not implemented
        self.sock.send_cmd(f'movej(pose_add(get_target_tcp_pose(), pose_sub({self.Go_Down_To_Grab_p}, {self.Go_Down_To_Grab_p})), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

        #Grab the piece
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        #self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movej({point}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

    def pick_up_from_corner(self):

        #go to corner pose
        self.sock.send_cmd(f'movej({None}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        #Go down to spot
        # pose not implemented
        self.sock.send_cmd(f'movej(pose_add(get_target_tcp_pose(), pose_sub({self.Go_Down_To_Grab_p}, {self.Go_Down_To_Grab_p})), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

        #Grab the piece
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        #self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time

        #Go up to corner pose
        self.sock.send_cmd(f'movej({None}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time


    def drop_in_plinko(self):

        #Go to reset point for the plinko slot
        self.sock.send_cmd(f'movej({self.Plinko_Reset_p}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time
        
        #Go to point above the plinko slot
        self.sock.send_cmd(f'movej({self.Plinko_Point1_p}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        self.gripper_close()

        
        
        
    def goto_reset(self):
        self.sock.send_cmd(f'movej({self.Uppiece_p}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5)
        
    def gripper_open(self):
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        #self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time
        
    def gripper_close(self):
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        #self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time

    # this is kinda lazy but i didnt want to mess with setting up server
    def run_command(self, command):
        self.sock.send_cmd(command)

        
