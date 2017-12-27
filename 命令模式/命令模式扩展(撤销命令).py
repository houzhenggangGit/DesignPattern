# -*- coding: UTF-8 -*-
'''
@author: Arron
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hou.zg@foxmail.com
@software: import
@file: 命令模式扩展(撤销命令).py
@time: 2017/12/24 0024 21:10
http://www.cnblogs.com/JsonShare/p/7206513.html
有两种基本的思路来实现可撤销的操作：

　　1、逆向操作实现：比如被撤销的操作是添加功能，那撤消的实现就变成删除功能；同理被撤销的操作是删除功能，那么撤销的实现就变成添加功能；

　　2、存储恢复实现，意思就是把操作前的状态记录下来，然后要撤销操作的时候就直接恢复回去就可以了，可使用备忘录模式(Memento Pattern)来实现（稍后会讲到备忘录模式）;

逆向操作来实现撤销(undo)：
具体操作：在命令模式中，我们可以通过调用一个命令对象的execute()方法来实现对请求的处理，如果需要撤销(undo)请求，可通过在命令类中增加一个逆向操作来实现。
'''
