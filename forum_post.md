



I have been working on a way to easily (and cheaply) design and include soft elements in poppy creatures. I came up with poppy-soft-connector:


The idea is simple: by embedding hard connectors into silicon based parts, we create soft part with a standard Ollo mechanical interface. These parts can they be used as plug and play building blocks.

To create the soft part you have to prepare a mold of the desired shape. The mold's wall should be 2.2mm thick (for Ollo rivets) and include Ollo holes at the position you would like to add the connectors. The connectors are then positioned into the mold and maintained in place using Ollo rivet. You can then pour the polymer of your choice into the mold and allow for enough time for the polymer to cure - thus embedding the connector into the part. The soft part can then be unmolded and attached with XL-320 motors or any Ollo parts to create 'soft robots'.

As an example, I built poppy-soft-starfish a simple 6 degrees of freedom robot with 3 arms. The connection between motors are all made out of silicon, giving quite interesting properties to the robot. I released the all hardware and software, as well as some videos showcasing the building process and my attempts to make it move.

While the starfish robot is not the best application of the soft links, it demonstrates how to use soft connectors. The possibilities are immense as many different kinds of polymer can be used with many different properties. It also allows to embed electronics, sensors, cables, and more into the body of our robots. The soft connector I designed is neither the smartest nor the only way to go but it is a good starting point. More specialized connectors will have to be designed for different applications. I propose that we share them all on the following repository: poppy-soft-connector.

I hope this will tickle the imagination and creativity of some of you. I am convinced it will open a new possibilities for artistic minded people!
