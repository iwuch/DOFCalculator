import PySimpleGUI as sg

Swich = True

while(Swich):

    form1 = sg.FlexForm('自由度结算器')
    layout = [
              #[sg.InputCombo(['男','女','隐私'],auto_size_text=True)],
              [sg.Text('d：系统阶数（平面运动填3，空间运动填6）', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('n：含基底的连杆和组件总数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('R：R副（旋转轴）数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('P：P副（平行轴）数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('C：C副（柱形轴）数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('H：H副（虎克铰）数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Text('S：S副（球形轴）数', size=(35,1)), sg.InputText('',size=(4,1))],
              [sg.Submit()]
             ]

    button, values = form1.Layout(layout).Read()

    d = int(values[0]) if values[0]!='' else 0
    n = int(values[1]) if values[1]!='' else 0
    R = int(values[2]) if values[2]!='' else 0
    P = int(values[3]) if values[3]!='' else 0
    C = int(values[4]) if values[4]!='' else 0
    H = int(values[5]) if values[5]!='' else 0
    S = int(values[6]) if values[6]!='' else 0

    g = R + P + C + H + S
    f = (R+P+2*(C+H)+3*S)
    DOF = d*(n-g-1)+f

    form1.Close()

    form2= sg.FlexForm('计算结果结果')
    layout = [[sg.Text('该机构的自由度为：', size=(16,1)),sg.Text(DOF)]]
    layout.append([sg.Text('------------------------------------')])
    layout.append([sg.Text('d：', size=(16,1)),sg.Text(d)])
    layout.append([sg.Text('n：', size=(16,1)),sg.Text(n)])
    layout.append([sg.Text('R：', size=(16,1)),sg.Text(R)])
    layout.append([sg.Text('P：', size=(16,1)),sg.Text(P)])
    layout.append([sg.Text('C：', size=(16,1)),sg.Text(C)])
    layout.append([sg.Text('H：', size=(16,1)),sg.Text(H)])
    layout.append([sg.Text('S：', size=(16,1)),sg.Text(S)])

    layout.append([sg.Text('Author:Wu Chenwei')])
    layout.append([sg.OK(),sg.Cancel()])
    button, values = form2.Layout(layout).Read()

    if button == 'Cancel':
        Swich = False

    form2.Close()


print("DOF=",DOF)
print("\nWhen:")
print("d =",d)
print("n =",n)
print("R =",R)
print("P =",P)
print("C =",C)
print("H =",H)
print("S =",S)

# print(button,type(button))