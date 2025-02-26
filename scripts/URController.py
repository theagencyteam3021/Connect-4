from scripts.server import URSocket
from scripts.robot import init_robot
import time

class URController:

    

    def __init__(self):
        self.sock = URSocket(debug=True)
        init_robot(self.sock)

        self.Uppiece_p='p[.283669258610, -.347648073463, .424146003192, .694771959431, 1.754634081148, -1.538764689241]'
        self.Uppiece_q='[-3.7996841112719935, -1.3526206028512497, 1.7858994642840784, 2.7835962015339355, -2.3331971804248255, 0.9564148783683777]'
        self.PickUp_from_p='p[.375739482937, -.086634922480, .042262099523, -.378230322671, 3.112559633039, .013042208682]'
        self.PickUp_to_p='p[.377848073688, -.085419996674, .022825539051, -.378246720523, 3.112584990394, .013056245636]'
        self.Moveaway_from_p='p[.386130121457, -.086636404499, .021374953430, -.378130646312, 3.112636447661, .013028787136]'
        self.Moveaway_to_p='p[.386134135970, -.086627753675, .045107121874, -.378222226500, 3.112584802764, .013036704789]'
        self.Reset_p='p[.283658307565, -.347660256071, .424117552911, .694819419243, 1.754722016139, -1.538816710004]'
        self.Reset_q='[-3.799697462712423, -1.3525857639363785, 1.7859233061419886, 2.783622904414795, -2.3332553545581263, 0.9564146995544434]'
        self.High1_p='p[.368188117232, -.420566120199, .386478704207, .758026102238, 1.773664338316, -1.672316893258]'
        self.High1_q='[-3.769541088734762, -0.7186911267093201, 0.9843147436725062, 2.9451376634785156, -2.4852476755725306, 0.8912343978881836]'
        self.Setdown_from_p='p[.368189332974, -.420572372214, .386477734558, .757995392526, 1.773716570238, -1.672337576525]'
        self.Setdown_to_p='p[.368488189835, -.420330292965, .338455369852, .757284674676, 1.773795792665, -1.671838722219]'
        self.Setup_from_p='p[.368185691159, -.420565915416, .338487130527, .758018932415, 1.773693887809, -1.672339406733]'
        self.Setup_to_p='p[.368176896763, -.420584486545, .387693022958, .758060061407, 1.773696302070, -1.672376836552]'
        self.High2_p='p[.334407450813, -.420549198774, .386489992450, .758054760718, 1.773628009788, -1.672303938357]'
        self.High2_q='[-3.8238914648639124, -0.8636584442904969, 1.2522524038897913, 2.817692919368408, -2.431126896535055, 0.8854033350944519]'
        self.High3_p='p[.299121598593, -.420560726236, .386496385912, .758048207498, 1.773640049062, -1.672317135954]'
        self.High3_q='[-3.8912950197802942, -0.996677891617157, 1.4856398741351526, 2.712817831630371, -2.363913361226217, 0.8791136741638184]'
        self.High4_p='p[.262595772792, -.420545384667, .386504647803, .758017464115, 1.773608437458, -1.672276171448]'
        self.High4_q='[-3.9758108297931116, -1.1255344611457367, 1.6978033224688929, 2.6250321108051757, -2.2795098463641565, 0.8723981380462646]'
        self.High5_p='p[.231938583764, -.417630990991, .386498624945, .757951046416, 1.773652978775, -1.672326430911]'
        self.High5_q='[-4.055077854787008, -1.2363885206035157, 1.8671262899981897, 2.5632945734211425, -2.2003448645221155, 0.8668502569198608]'
        self.High6_p='p[.198150721519, -.416348811027, .386501977385, .757998115801, 1.773640751472, -1.672323542629]'
        self.High6_q='[-4.168552939091818, -1.3583070647767563, 2.0364421049701136, 2.5123941141315917, -2.0870145002948206, 0.860062837600708]'
        self.High7_p='p[.159247263452, -.415198421044, .388083510785, .758084544757, 1.773542092106, -1.672425663359]'
        self.High7_q='[-4.339349691067831, -1.513744906788208, 2.213288132344381, 2.487506552333496, -1.9164493719684046, 0.8512888550758362]'
        self.Plinko_Reset_p='p[.344200881006, -.333937468008, .744468401573, .221533876087, 1.514098284181, -1.372686352557]'
        self.Plinko_Reset_q='[-4.076216046010153, -1.1923377376845856, 0.2538488546954554, 3.888868494624756, -1.6176698843585413, 0.8710737824440002]'
        self.Plinko_Point1_p='p[.595962463701, -.201904714105, .606146446172, -1.004933677079, 1.379785948807, -.995298248346]'
        self.Plinko_Point1_q='[-4.08470589319338, -0.8768575948527833, 0.2541125456439417, 3.827688379878662, -0.6530912558185022, 0.23826520144939423]'

        # incomplete: add relative movement to grab piece off plate
        self.Go_Down_To_Grab_p='[]'

        self.board_points = [self.High1_p, self.High2_p, self.High3_p, self.High4_p, self.High5_p, self.High6_p, self.High7_p]
        self.board_poses = [self.High1_q, self.High2_q, self.High3_q, self.High4_q, self.High5_q, self.High6_q, self.High7_q]

    def drop_in_column(self, column_number, reset_before = True, reset_after = True):
        point = self.board_points[column_number - 1]
        pose = self.board_points[column_number - 1]

        if reset_before:
            self.sock.send_cmd(f'movej(get_inverse_kin({self.Reset_p}, qnear={self.Reset_q}), a=1.3962634015954636, v=1.0471975511965976)')
            time.sleep(5)

        #Go to point above the correct column
        self.sock.send_cmd(f'movej({point}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5) #TODO tune this time

        #Go down into the slot
        self.sock.send_cmd(f'movej(pose_add(get_target_tcp_pose(), pose_sub({self.Setdown_to_p}, {self.Setdown_from_p})), a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time

        #Drop the piece
        self.sock.send_cmd('set_standard_digital_out(1, False)')
        self.sock.send_cmd('set_standard_digital_out(5, False)')
        time.sleep(1) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movej({point}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time
        
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
        self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time

        #Go back up
        self.sock.send_cmd(f'movej({point}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(2) #TODO tune this time
        
        
        
    def goto_reset(self):
        self.sock.send_cmd(f'movej({self.Reset_p}, a=1.3962634015954636, v=1.0471975511965976)')
        time.sleep(5)
        
    def gripper_open(self):
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time
        
    def gripper_close(self):
        self.sock.send_cmd('set_standard_digital_out(1, True)')
        self.sock.send_cmd('set_standard_digital_out(5, True)')
        time.sleep(1) #TODO tune this time
        


