command = '''
set_safety_mode_transition_hardness(1)
modbus_add_signal("192.168.1.3", 255, 1, 0, "MODBUS_1", False)
modbus_set_signal_update_frequency("MODBUS_1", 10)
modbus_add_signal("192.168.1.3", 255, 1, 1, "MODBUS_2", False)
modbus_set_signal_update_frequency("MODBUS_2", 10)
modbus_set_runstate_dependent_choice("MODBUS_2",0)
set_standard_analog_input_domain(0, 1)
set_standard_analog_input_domain(1, 1)
set_tool_analog_input_domain(0, 1)
set_tool_analog_input_domain(1, 1)
set_analog_outputdomain(0, 0)
set_analog_outputdomain(1, 0)
set_input_actions_to_default()
set_tcp(p[-0.018457705833652818,-0.06671608895162245,0.19891377627880122,0.0,0.0,0.0])
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
