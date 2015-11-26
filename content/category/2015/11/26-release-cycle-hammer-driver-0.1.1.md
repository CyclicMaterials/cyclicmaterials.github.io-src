Title: Detect touch gestures with Cycle.js and Hammer.js
Date: 2015-11-26 15:07:00
Authors: Frederik Krautwald
Category: Releases
Tags: release, patch, driver, hammer, cycle, touch, gesture
Slug: release-cycle-hammer-driver-0.1.1
Summary: cycle-hammer-driver version 0.1.1 is out

[Hammer.js][hammerjs] is a small (~4 KB) and highly performable touch-gesture library. 
It let’s you hassle-free detect tough gestures such as pan, press, rotate, 
swipe, tap, and pinch. However, as [Cycle.js][cyclejs] separates IO from 
the main program, a driver was needed to encapsulate Hammer.js. 
At Cyclic Materials, we set out to solve this.

We are happy to announce [cycle-hammer-driver version 0.1.1][1].

From the outset, we didn’t want to change the way Cycle.js users listen 
for DOM events, e.g., `DOM.select('#MyElement').events('click')`. But we also 
didn’t want the driver to depend on a specific DOM driver; only the interface. 
To achieve this, we let the user decide which DOM driver they want to use and 
then pass it to the Hammer driver. A benefit of this approach is that no code 
changes are needed for it to work with existing code that uses a DOM driver.

```js
const domDriverFunc = makeDOMDriver('#app')

const sources = {
  DOM: makeHammerDriver(domDriverFunc)
}

Cycle.run(main, sources)
```

The Hammer driver effectively augments the `events()` function of the DOM driver 
to listen for Hammer events. When you listen for Hammer events, the Hammer 
driver internally creates an instance of `Hammer.Manager` 
for the selected element, but the driver provides a way to gain access 
to the instance. This happens through an optional callback you can pass 
as the second argument to the `events()` function.

```js
DOM.select(<String>selector).events(<String>hammerEventType, <Function>callback)
```

The `callback` function is invoked with the `Hammer.Manager` instance 
and a reference to the `Hammer` namespace object.

```js
<Function>callback(manager<object>, Hammer<object>)
```

From the basic example, which you can find in the repo, we use the Hammer 
driver like this:

```js
function intent(DOM) {
  const options = (manager, Hammer) => {
    // Default pan recognizer.
    manager.add(new Hammer.Pan())
    // Default tap recognizer.
    manager.add(new Hammer.Tap())
    // Default press recognizer.
    manager.add(new Hammer.Press())
  }
  return {
    events$: Observable.merge(
      DOM.select(`#MyElement`).events(`panleft`, options),
      DOM.select(`#MyElement`).events(`panright`),
      DOM.select(`#MyElement`).events(`tap`),
      DOM.select(`#MyElement`).events(`press`)
    ),
  }
}
```

Now it’s time for you to take [Cycle.js][cyclejs] for a spin with this amazing 
driver. Head over to the repository to [download this release][1]. You can also 
obtain it through *npm* by issuing the following command in your terminal:

```shell
$ npm i @cyclic/cycle-hammer-driver@0.1.1
```

Don’t forget to check the *examples* directory in the repo, and read 
the [official Hammer.js documentation][hammerjs] to find out what you can do. 



[1]: https://github.com/CyclicMaterials/cycle-hammer-driver/releases/tag/v0.1.1
[hammerjs]: https://hammerjs.github.io/
[cyclejs]: http://cycle.js.org/
