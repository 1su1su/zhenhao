'''IS-7火箭冲锋队'''
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

# st(background_image = Image.open("宇宙.gif"))

page = st.sidebar.radio('IS-7火箭冲锋队', ['首页', '科技树', '精彩对局', '车辆数值', '我的留言区', '我的图片处理工具','单词查询'])

def page_1():
    '''首页'''
    st.write("欢迎各位车长光临本站，请大家多多支持~~")
    st.write("本站内容仅参考")
    with open(r'第一层.mp3', 'rb') as f:
        mymp3_1 = f.read()
    st.audio(mymp3_1, format='audio/mp3', start_time=0)
    st.image('1.jpg')
    st.write("《坦克世界》：")
    st.write("《坦克世界》（World of Tanks）是一款在2010年由Wargaming公司推出的战争网游。")
    st.write("2020年3月12日， 360联合Wargaming、空中网，三家共同召开“战火重燃”网络发布会，正式宣布360和空中网深度联运Wargaming旗下军武游戏《坦克世界》、《战舰世界》，并公布游戏内容将在今年内实现与国际版本同步更新。")
    st.write("在游戏中，玩家会扮演1930到1960年代的战车进行对战（PvP），高度要求战略和合作性。")
    st.write("目前已有苏联、德国、美国、英国、法国、中国、日本、捷克、瑞典、波兰以及意大利的战车可供玩家选用，预计未来版本会推出欧洲联合，以色列等国家战车，游戏中的战车根据历史高度还原，预计将有共约500台战车。")
    st.write("游戏2010年10月30日在俄罗斯首发，2011年4月12日在北美和欧洲推出，中国大陆于2011年3月15日推出。目前全球用户超过6000万。")
    st.write("2020年，《坦克世界》战火重燃， 360定能不负玩家所爱，再造军武游戏的辉煌。")
    st.write("(○｀ 3′○)：最后这句纯属瞎逼逼！")


def page_2():
    '''科技树'''
    st.write('C系')
    st.image('科技树C.png')
    st.write('S系')
    st.image('科技树S.png')
    st.write('D系')
    st.image('科技树D.png')
    st.write('M系')
    st.image('科技树M.png')
    st.write('F系')
    st.image('科技树F.png')
    st.write('Y系')
    st.image('科技树Y.png')
    st.write('R系')
    st.image('科技树R.png')
    st.write('J系')
    st.image('科技树J.png')
    st.write('B系')
    st.image('科技树B.png')
    st.write('V系')
    st.image('科技树V.png')
    st.write('I系')
    st.image('科技树I.png')
    

def page_3():
    '''精彩对局'''
    st.write('精选up主：')
    st.link_button('我是车长舒克', 'https://space.bilibili.com/3391988?spm_id_from=333.337.search-card.all.click')
    st.link_button('坦克世界_汤圆', 'shttps://space.bilibili.com/337084279?spm_id_from=333.337.0.0')

def page_4():
    '''车辆数值'''
    go_1 = st.selectbox('选择想要查看的C系坦克（目前仅限银币车）', ['雷诺 NC-31', '维克斯 Mk.E', '97式', 'M5A1', '59-16', 'WZ131', 'WZ132', 'WZ132A', 'WZ132-1', 'T-34*', '58式', 'T-34-1', 'T-34-2', 'WZ120',
                                                               '121', 'IS-2', 'BZ-58', '110', 'BZ-166', '111 1-V', 'BZ-68','113', '111 5A', 'BZ-75', 'T-26G', 'M3G', 'SU-76G', '60G', 'WZ131G', 'T-34-2G',
                                                               'WZ111-1G', 'WZ111G', 'WZ113G'])
    if go_1 == '雷诺 NC-31':
        st.image('局部截取_20240722_190234.png')
        st.image('局部截取_20240722_190252.png')
    elif go_1 == '维克斯 Mk.E':
        st.iamge('局部截取_20240722_190441.png')
        st.image('局部截取_20240722_190519.png')
    elif go_1 == '97式':
        st.iamge('局部截取_20240722_190708.png')
        st.image('局部截取_20240722_190739.png')
    elif go_1 == 'M5A1':
        st.iamge('局部截取_20240722_190929.png')
        st.image('局部截取_20240722_190945.png ')
    elif go_1 == '59-16':
        st.iamge('局部截取_20240722_192626.png')
        st.image('111116.png')
    elif go_1 == 'WZ131':
        st.iamge('局部截取_20240722_192916.png')
        st.image('局部截取_20240722_192934.png')
    elif go_1 == 'WZ132':
        st.iamge('局部截取_20240722_193057.png')
        st.image('局部截取_20240722_193110.png')
    elif go_1 == 'WZ132A':
        st.iamge('局部截取_20240722_193223.png')
        st.image('局部截取_20240722_193250.png')
    elif go_1 == 'WZ132-1':
        st.iamge('局部截取_20240722_193434.png')
        st.image('局部截取_20240722_193447.png')
    elif go_1 == 'T-34*':
        st.iamge('局部截取_20240722_193612.png')
        st.image('局部截取_20240722_193631.png')
    elif go_1 == '58式':
        st.iamge('局部截取_20240722_193758.png')
        st.image('局部截取_20240722_193811.png')
    elif go_1 == 'T-34-1':
        st.iamge('局部截取_20240722_200233.png')
        st.image('局部截取_20240722_200253.png')
    elif go_1 == 'T-34-2':
        st.iamge('局部截取_20240722_200450.png')
        st.image('局部截取_20240722_200502.png')
    elif go_1 == 'WZ120':
        st.iamge('局部截取_20240722_200627.png')
        st.image('局部截取_20240722_200639.png')
    elif go_1 == '121':
        st.image('局部截取_20240722_200751.png')
        st.iamge('局部截取_20240722_200803.png')
    elif go_1 == 'IS-2':
        st.image('局部截取_20240722_200921.png')
        st.iamge('局部截取_20240722_200931.png')
    elif go_1 == 'BZ-58':
        st.image('局部截取_20240722_201036.png')
        st.iamge('局部截取_20240722_201050.png')
    elif go_1 == '110':
        st.image('局部截取_20240722_201158.png')
        st.iamge('局部截取_20240722_201220.png')
    elif go_1 == 'BZ-166':
        st.image('局部截取_20240722_201332.png')
        st.iamge('局部截取_20240722_201347.png')
    elif go_1 == '111 1-V':
        st.image('局部截取_20240722_201518.png')
        st.iamge('局部截取_20240722_201543.png')
    elif go_1 == 'BZ-68':
        st.image('局部截取_20240722_201739.png')
        st.iamge('局部截取_20240722_201751.png')
    elif go_1 == '113':
        st.image('局部截取_20240722_201856.png')
        st.iamge('局部截取_20240722_201922.png')
    elif go_1 == '111 5A':
        st.image('局部截取_20240722_202028.png')
        st.iamge('局部截取_20240722_202049.png')
    elif go_1 == 'BZ-75':
        st.image('局部截取_20240722_202157.png')
        st.iamge('局部截取_20240722_202207.png')
    #elif go_1 == 'T-26G':
    #    st.image('')
    #    st.iamge('')
    #elif go_1 == 'M3G':
    #    st.image('')
    #    st.iamge('')
    #elif go_1 == 'SU-76G':
    #     st.image('')
    #    st.iamge('')
    #elif go_1 == '60G':
    #    st.image('')
    #    st.iamge('')
    #elif go_1 == 'WZ131G':
    #    st.image('')
    #    st.iamge('')
    #elif go_1 == 'T-34-2G':
    #     st.image('')
    #     st.iamge('')
    # elif go_1 == 'WZ111-1G':
    #     st.image('')
    #     st.iamge('')
    # elif go_1 == 'WZ111G':
    #     st.image('')
    #     st.iamge('')
    # elif go_1 == 'WZ113G':
    #     st.image('')
    #     st.iamge('')

    go_2 = st.selectbox('选择想要查看的S系坦克（目前仅限银币车）', ['MS-1', 'BT-2', 'T-26', 'T-60', 'T-46', 'T-70', 'BT-5','T-70', 'BT-7', 'T-80', 'A-20', 'T-50', 'MT-25', 'LTG', 'LTTB', 'T-54轻型', 'T-100 LT',
                                                               'T-28', 'T-34', 'T-34-85', 'A-43', 'T-43', 'KV-13', 'A-44', 'T-44', '416工程', 'T-54', '430工程||型', '430工程', 'T-62A', '140工程', '430工程U',
                                                               'K-91', 'KV-1', 'KV-85', 'KV-2', 'T-150', 'KV-1S', 'IS', 'KV-3','IS-3', 'KV-4', 'IS-M','IS-2-||','ST-1', 'T-10', '257工程', '705工程', 'IS-3-||',
                                                               'IS-4', 'IS-7', '705工程A', '277工程', 'ST-II', 'AT-1','SU-76M','SU-85B','SU-85','SU-100','SU-152','SU-100M1','ISU-152','SU-101','704工程',
                                                               '263工程','268工程','268工程IV型','SU-18','SU-26','SU-5','SU-122A','SU-8','S-51','SU-14-1','SU-14-2','212工程','261工程'])
    #go = st.selectbox('选择想要查看的D系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的M系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的F系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的Y系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的I系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的J系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的B系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的V系坦克（目前仅限银币车）', [, ])
    #go = st.selectbox('选择想要查看的I系坦克（目前仅限银币车）', [, ])
    st.image('2.jpg')

def page_5():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件夹中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('😄'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🙎‍♂️'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……',['车长','炮手', '观察手', '驾驶员', '装填手'])
    new_message = st.text_input("想要说的话……")
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
                

def page_6():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpg','jpeg'])
    if uploaded_file:
        # 获取图片的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img))

def page_7():
    '''单词询查'''
    st.write('单词查询')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将本地文件的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    #从本地文件中将单词是查询次数读取出来，并储存在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as t:
        times_list = t.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    time_dict = {}
    for i in times_list:
        time_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词：')
    # print(words_dict)
    # 现实查询的内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in time_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('询查次数：', time_dict[n])

def img_change(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            img_array[x,y] = (b,g,r)
    return img

if page == '首页':
    page_1()
elif page == '科技树':
    page_2()
elif page == '精彩对局':
    page_3()
elif page == '车辆数值':
    page_4()
elif page == '我的留言区':
    page_5()
elif page == '我的图片处理工具':
    page_6()
elif page == '单词查询':
    page_7()
