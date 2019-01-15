# Poppy Soft Starfish

poppy-soft-starfish is the first robot showcasing the use of [poppy-soft-connector](https://github.com/poppy-project/poppy-soft-connector) to create flexible robotic parts.

![forward_side_view](doc/gif/forward_side_view.gif)

Discussions about this project are located on [this post](https://forum.poppy-project.org/t/poppy-soft-connector/2152) of [our forum](https://forum.poppy-project.org/).

## Principles 

The idea is simple: by embedding hard connectors into silicon based parts, we create soft part with a standard Ollo mechanical interface. These parts can they be used as plug and play building blocks. See [tutorial video](https://youtu.be/B3CZs55AJQo).

To create the soft part you have to prepare a mold of the desired shape. The mold's wall should be 2.2mm thick (for Ollo rivets) and include Ollo holes at the position you would like to add the connectors. The connectors are then positioned into the mold and maintained in place using Ollo rivet. You can then pour the polymer of your choice into the mold and allow for enough time for the polymer to cure - thus embedding the connector into the part. The soft part can then be unmolded and attached with XL-320 motors or any Ollo parts to create 'soft robots'. The starfish robot demonstrates how to use soft connectors.

The possibilities are immense as many different kinds of polymer can be used with many different properties. It also allows to embed electronics, sensors, cables, and more into the body of our robots. I hope this will tickle the imagination and creativity of some of you. I am convinced it will open new possibilities for artistic minded people!

## More information

- [Tutorial video](https://youtu.be/B3CZs55AJQo)
- [doc folder](doc) for building instructions and help
- [hardware folder](hardware) for the mechanical parts
- [software folder](software) for code examples


### Contributing

Create your own soft robot and share it on [our forum](https://forum.poppy-project.org/)!

You can also propose new optimized design for the [poppy-soft-connector](https://github.com/poppy-project/poppy-soft-connector).

To contribute to this repository, you can [fork it](https://help.github.com/articles/fork-a-repo/) and issue a [pull request](https://help.github.com/articles/using-pull-requests/). [[Another useful link]](https://gun.io/blog/how-to-github-fork-branch-and-pull-request/)


### License

All the technological development work made in the Poppy project is freely available under open source licenses. Only the name usage *"Poppy"* is restricted and protected as an international trademark, please contact us if you want to use it or have more information.

|   License     |     Hardware    |   Software      |
| ------------- | :-------------: | :-------------: |
| Title  | [Creatives Commons BY-SA](http://creativecommons.org/licenses/by-sa/4.0/)  |[GPL v3](http://www.gnu.org/licenses/gpl.html)  |
| Logo  | [![Creative Commons BY-SA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png) ](http://creativecommons.org/licenses/by-sa/4.0/)  |[![GPL V3](https://www.gnu.org/graphics/gplv3-88x31.png)](http://www.gnu.org/licenses/gpl.html)  |
