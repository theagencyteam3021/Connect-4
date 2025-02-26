from server-side import URSocket

command = '''
set_tcp(p[-0.018457705833652818,-0.06671608895162245,0.19891377627880122,0.0,0.0,0.0])
set_safety_mode_transition_hardness(1)
set_target_payload(1.370000, [0.020000, -0.023000, 0.016000], [0.002601, 0.002601, 0.002601, 0.000000, 0.000000, 0.000000])
set_standard_analog_input_domain(0, 1)
set_standard_analog_input_domain(1, 1)
set_tool_analog_input_domain(0, 1)
set_tool_analog_input_domain(1, 1)
set_analog_outputdomain(0, 0)
set_analog_outputdomain(1, 0)
set_input_actions_to_default()
set_gravity([0.0, 0.0, 9.82])
set_tool_communication(False, 115200, 0, 1, 1.5, 3.5)
set_tool_output_mode(0)
set_tool_digital_output_mode(0, 1)
set_tool_digital_output_mode(1, 1)
set_tool_voltage(0)
'''

def init_robot(sock):
    for line in command.split('\n'):
        sock.send_cmd(line)
