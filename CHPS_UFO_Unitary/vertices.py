# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 15 May 2019 10:43:19


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_19})

V_2 = Vertex(name = 'V_2',
             particles = [ P.ghWm, P.ghWm__tilde__, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_15})

V_3 = Vertex(name = 'V_3',
             particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_16})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_22})

V_5 = Vertex(name = 'V_5',
             particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_18})

V_6 = Vertex(name = 'V_6',
             particles = [ P.ghWp, P.ghWp__tilde__, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_17})

V_7 = Vertex(name = 'V_7',
             particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_16})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_21})

V_9 = Vertex(name = 'V_9',
             particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_23})

V_10 = Vertex(name = 'V_10',
              particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_20})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_24})

V_12 = Vertex(name = 'V_12',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[ghWi]], P.<>CreateObjectParticleName[PartNameMG[ghWibar]], P.<>CreateObjectParticleName[PartNameMG[Wi]] ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_32})

V_13 = Vertex(name = 'V_13',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_74})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_7})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.Z, P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_13})

V_16 = Vertex(name = 'V_16',
              particles = [ P.Z, P.Z, P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_14})

V_17 = Vertex(name = 'V_17',
              particles = [ P.g, P.g, P.eta ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_8})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.g, P.eta ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_9})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_4})

V_21 = Vertex(name = 'V_21',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_6,(0,0):C.GC_6,(2,2):C.GC_6})

V_22 = Vertex(name = 'V_22',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.<>CreateObjectParticleName[PartNameMG[LL]], P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_45})

V_23 = Vertex(name = 'V_23',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.<>CreateObjectParticleName[PartNameMG[QL]], P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_44})

V_24 = Vertex(name = 'V_24',
              particles = [ P.eta, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_33})

V_25 = Vertex(name = 'V_25',
              particles = [ P.a, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_61})

V_26 = Vertex(name = 'V_26',
              particles = [ P.a, P.a, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_71})

V_27 = Vertex(name = 'V_27',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_66})

V_28 = Vertex(name = 'V_28',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_70})

V_29 = Vertex(name = 'V_29',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.u, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_28})

V_30 = Vertex(name = 'V_30',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.c, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_29})

V_31 = Vertex(name = 'V_31',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.t, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_30})

V_32 = Vertex(name = 'V_32',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.u, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_25})

V_33 = Vertex(name = 'V_33',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.c, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_26})

V_34 = Vertex(name = 'V_34',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.t, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_27})

V_35 = Vertex(name = 'V_35',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.d, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_58})

V_36 = Vertex(name = 'V_36',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.s, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_59})

V_37 = Vertex(name = 'V_37',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.b, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_60})

V_38 = Vertex(name = 'V_38',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.d, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_52})

V_39 = Vertex(name = 'V_39',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.s, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_53})

V_40 = Vertex(name = 'V_40',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.b, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_54})

V_41 = Vertex(name = 'V_41',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.e__minus__, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_55})

V_42 = Vertex(name = 'V_42',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.mu__minus__, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_56})

V_43 = Vertex(name = 'V_43',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.ta__minus__, P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_57})

V_44 = Vertex(name = 'V_44',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.e__minus__, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_49})

V_45 = Vertex(name = 'V_45',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.mu__minus__, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_50})

V_46 = Vertex(name = 'V_46',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.ta__minus__, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_51})

V_47 = Vertex(name = 'V_47',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.<>CreateObjectParticleName[PartNameMG[QL]], P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_46})

V_48 = Vertex(name = 'V_48',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Wi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_43})

V_49 = Vertex(name = 'V_49',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.<>CreateObjectParticleName[PartNameMG[LL]], P.<>CreateObjectParticleName[PartNameMG[Wi]] ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_43})

V_50 = Vertex(name = 'V_50',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VSS1, L.VSS3 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_40})

V_51 = Vertex(name = 'V_51',
              particles = [ P.a, P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_37})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_42})

V_53 = Vertex(name = 'V_53',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_38})

V_54 = Vertex(name = 'V_54',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_39})

V_55 = Vertex(name = 'V_55',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]] ],
              color = [ '1' ],
              lorentz = [ L.VVVV2, L.VVVV5, L.VVVV6 ],
              couplings = {(0,1):C.GC_75,(0,2):C.GC_76,(0,0):C.GC_77})

V_56 = Vertex(name = 'V_56',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.eta ],
              color = [ '1' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_31})

V_57 = Vertex(name = 'V_57',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]], P.<>CreateObjectParticleName[PartNameMG[Wi]] ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_32})

V_58 = Vertex(name = 'V_58',
              particles = [ P.d__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_63})

V_59 = Vertex(name = 'V_59',
              particles = [ P.s__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_64})

V_60 = Vertex(name = 'V_60',
              particles = [ P.b__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_65})

V_61 = Vertex(name = 'V_61',
              particles = [ P.d__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_67})

V_62 = Vertex(name = 'V_62',
              particles = [ P.s__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_68})

V_63 = Vertex(name = 'V_63',
              particles = [ P.b__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_69})

V_64 = Vertex(name = 'V_64',
              particles = [ P.e__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_78})

V_65 = Vertex(name = 'V_65',
              particles = [ P.mu__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_80})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_82})

V_67 = Vertex(name = 'V_67',
              particles = [ P.e__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_79})

V_68 = Vertex(name = 'V_68',
              particles = [ P.mu__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_81})

V_69 = Vertex(name = 'V_69',
              particles = [ P.ta__plus__, P.<>CreateObjectParticleName[PartNameMG[LL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phibar]] ],
              color = [ '1' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_83})

V_70 = Vertex(name = 'V_70',
              particles = [ P.u__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_84})

V_71 = Vertex(name = 'V_71',
              particles = [ P.c__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_86})

V_72 = Vertex(name = 'V_72',
              particles = [ P.t__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_88})

V_73 = Vertex(name = 'V_73',
              particles = [ P.u__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_85})

V_74 = Vertex(name = 'V_74',
              particles = [ P.c__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_87})

V_75 = Vertex(name = 'V_75',
              particles = [ P.t__tilde__, P.<>CreateObjectParticleName[PartNameMG[QL]], P.eta, P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2 ],
              couplings = {(0,0):C.GC_89})

V_76 = Vertex(name = 'V_76',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[LLbar]], P.<>CreateObjectParticleName[PartNameMG[LL]], P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_48})

V_77 = Vertex(name = 'V_77',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[QLbar]], P.<>CreateObjectParticleName[PartNameMG[QL]], P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_47})

V_78 = Vertex(name = 'V_78',
              particles = [ P.Z, P.eta, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_34})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Z, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_62})

V_80 = Vertex(name = 'V_80',
              particles = [ P.a, P.Z, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_72})

V_81 = Vertex(name = 'V_81',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.Z, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_36})

V_82 = Vertex(name = 'V_82',
              particles = [ P.<>CreateObjectParticleName[PartNameMG[Wi]], P.Z, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_41})

V_83 = Vertex(name = 'V_83',
              particles = [ P.Z, P.Z, P.<>CreateObjectParticleName[PartNameMG[Phibar]], P.<>CreateObjectParticleName[PartNameMG[Phi]] ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_73})

V_84 = Vertex(name = 'V_84',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1})

V_85 = Vertex(name = 'V_85',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1})

V_86 = Vertex(name = 'V_86',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1})

V_87 = Vertex(name = 'V_87',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_10})

V_88 = Vertex(name = 'V_88',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_10})

V_89 = Vertex(name = 'V_89',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_10})

V_90 = Vertex(name = 'V_90',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3})

V_91 = Vertex(name = 'V_91',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3})

V_92 = Vertex(name = 'V_92',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3})

V_93 = Vertex(name = 'V_93',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_12})

V_94 = Vertex(name = 'V_94',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_12})

V_95 = Vertex(name = 'V_95',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_12})

V_96 = Vertex(name = 'V_96',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2})

V_97 = Vertex(name = 'V_97',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_2})

V_99 = Vertex(name = 'V_99',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_11})

V_100 = Vertex(name = 'V_100',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_11})

V_101 = Vertex(name = 'V_101',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_11})

V_102 = Vertex(name = 'V_102',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

V_103 = Vertex(name = 'V_103',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

V_104 = Vertex(name = 'V_104',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

V_105 = Vertex(name = 'V_105',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

V_106 = Vertex(name = 'V_106',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

V_107 = Vertex(name = 'V_107',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_5})

