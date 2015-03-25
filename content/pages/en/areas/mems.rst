Gaseous and multiphase flows in MEMS
------------------------------------

:slug: areas/mems
:status: hidden
:lang: en

|

Recent trends in the space community for smaller, cheaper and more frequent space 
missions have driven the development of micro- and nanosatellites. The use of small 
spacecraft constellations is an attempt to enhance the overall performance of 
communication and remote sensing tasks currently done by a relatively small number 
of large platforms. Because micro-technologies have the advantage of reducing the 
total resources required on a spacecraft, the continued development of micro-technologies 
for space applications will further enable small satellite missions. Nanosatellites 
(mass between 1 and 10 kg) impose significant limitations on mass, power and volume
available for all subsystems including propulsion. In recent years, micropropulsion 
systems have been developed to address this need. A wide array of concepts will 
require the expansion of propellant gases through microscale nozzles. Because 
many micropropulsion systems will also operate at relatively low pressures, the 
investigation of low-Reynolds-number nozzle and jet flows has become increasingly
important for realistic evaluation of new concepts.

It is planned to perform a series of experimental and numerical studies of supersonic 
flows in micronozzles, which are an important element of thrusters of micro- and 
nanosatellites. Research work includes the development of technologies for manufacturing 
of supersonic micron-sized nozzle and the development of diagnostics of mass flow 
and momentum flux distribution in the micronozzles and the exhausting jets of gas 
mixtures. In addition, it is expected to obtain the integral characteristics of 
the micronozzles, such as specific impulse, thrust and time of engine thrust. The 
goal of this work is to increase the specific thrust of microjet engines, which 
should prolong the time of functioning of micro-and nanosatellites and increase 
the accuracy of their control. Numerically, Navier-Stokes, BGK and DSMC codes will 
be used to simulate inert, chemically reacting, and multi-phase flows in micronozzles 
and microjets. Plane, axisymmetric, and 3D micronozzles will be studied. Numerical 
simulations will be aimed at elucidating flow features in micronozzles and exhausting 
jets. For chemical and electrothermal micropropulsion devices, the fluid mechanics 
of reduced length scales (low Reynolds numbers) results in a significant degradation 
of the thrust efficiency as a result of increased viscous and heat-transfer losses. 
Numerical and experimental investigation of fluid flow and performance of micronozzles 
will be conducted in order to realistically evaluate the new micropropulsion concepts. 
Careful attention will be paid to the determination of characteristics of propulsion 
systems that scale favorably with reduced size. Advanced gas-surface interaction 
models will be implemented into the GPU-based DSMC code, validated against experiments 
and effects of nozzle surface roughness on the microthruster performance will be 
studied. 

A rapid progress in micromachining techniques during the last two decades 
has resulted in the fabrication and utilization of micro-electromechanical systems 
(MEMS) and nano-electromechanical systems (NEMS). Many micromachines, such as micropumps,
microturbines, microvalves, etc. involve flows of gases both in the subsonic and 
supersonic speed ranges. Due to very small sizes of MEMS, flows in them have many 
important features that differ from those in macromachines. Of particular interest 
in the development of MEMS is the design of the devices that are able to produce 
mechanical work from chemical heat release, i.e. micro-engines. At the microlevel, 
the time scales associated with heat loss mechanisms are reduced dramatically while 
the characteristic time scales for heat release stay virtually independent of the 
size. Thus, the efficiency of conventional devices such as internal combustion engines 
and gas turbines is seriously degraded when they are scaled to small sizes. One 
possibility to overcome this difficulty is to increase the rapidity of heat release 
using shock-induced (and/or shock-assisted) combustion. However, this technique 
requires a deeper insight into the mechanisms governing the microscale shock wave 
phenomena. Effects of viscosity and heat conduction, heat losses due to the wall 
heat transfer as well as non-equilibrium phenomena observed in rarefied flows are 
of importance for the shock wave propagation and interaction at microscales while 
they can be usually neglected for macro-scale shock waves. This requires better 
understanding of physical and chemical processes associated with propagation of 
shock and detonation waves at small scales. There is a significant current effort 
in this direction; in particular, the beginning of activities aimed at creating 
a microscopic test facility (shock tube 10 μm in diameter) was announced. Some 
recent publications also deal with microdetonics – processes that occur during 
detonation of microscopic amounts of explosives. Interesting results were obtained 
in experimental research of propagation of detonation waves in capillary tubes 
(V.I. Manzhalei, Lavrentyev Institute of Hydrodynamics, Siberian Branch, Russian 
Academy of Sciences, 1992-1999); in particular, Manzhalei found that detonation 
waves under such conditions can propagate with velocities that are only 0.45-0.6 
of the Chapman-Jouguet velocity. It should be noted that propagation of detonation 
waves in thin capillary tubes is important for explosion safety problems.

For Knudsen numbers Kn ~ 0.01 and higher, the continuum approach has to be used 
with caution, and the results have to be verified through comparisons with the 
kinetic approach. Thus, it is necessary to use the kinetic approach, namely, the 
DSMC method, to study detonation at microscopic scales, where the characteristic 
Knudsen numbers can exceed 0.01. In the framework of the proposed research laboratory 
the structure of an unsteady detonation wave in microchannels will be studied
at the kinetic level with the use of the DSMC method. For this reason, the further 
development and numerical implementation of collision models and algorithms for 
the description of the kinetic mechanism for a hydrogen-oxygen mixture in the 
DSMC method will be carried out. In particular, recombination processes that 
require simulations of ternary collisions will be considered in detail.


.. class:: button small

.. class:: myw

`Back <../areas.html>`_
