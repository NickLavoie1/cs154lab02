a = pyrtl.Input(bitwidth=1, name='a')
b = pyrtl.Input(bitwidth=1, name='b') 

o = pyrtl.Output(bitwidth=1, name='o')

stop = pyrtl.WireVector(bitwidth=32, name='stop')

one = pyrtl.Const(1, bitwidth=2)
two = pyrtl.Const(2, bitwidth=2)


regA = pyrtl.Register(bitwidth=32, name='regA')
regB = pyrtl.Register(bitwidth=32, name='regB')
regReset = pyrtl.Register(bitwidth=2, name='regReset')

with pyrtl.conditional_assignment:
    with regReset==0: 
        regA.next |= a
	regReset.next |= one
	stop |= a
    with regReset==1: 
        regB.next |= b
	regReset.next |= two
	stop |= b
    with regReset==2: 
        regA.next |= b
	regB.next |= stop
	stop |= regA + regB

o <<= stop
