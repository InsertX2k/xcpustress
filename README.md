# ![xcpustress & strgensvc Icon](https://github.com/InsertX2k/xcpustress/assets/62176660/fdb4cc3a-9d84-49f8-a5ab-3be579bdb19c) xcpustress
A simple program written in Python to help you perform a stress test on your processor, inspired by [Advanced Password Generator by Mr.X](https://github.com/InsertX2k/apg)

## Screenshots
* `xcpustress.exe` on **Monster stress testing mode**  <br> ![XCPUStress on Monster test mode](https://github.com/InsertX2k/xcpustress/assets/62176660/5498b9a5-5ecb-4aed-b96f-535798238141) <br> **Hint:** You can always stop a running stress test by pressing <kbd>Ctrl</kbd> + <kbd>C</kbd> on the console window of the program or by executing the command `taskkill /f /im xcpustress_rstrhost.exe`

* CLI usage <br> ![xcpustress.exe CLI usage](https://github.com/InsertX2k/xcpustress/assets/62176660/575a3b63-b0a7-4524-8ee4-d02e01f64271)

## Available stress testing modes
* 1 -> performs a basic stress test, launches 1 instance of the stress test process, useful for very old computers with CPUs slower than 1 GHz
* 2 -> performs a more advanced stress test, launches 3 instances of the stress test process, useful for old computers with CPUs slower than 2 GHz
* 3 -> performs an even more advanced stress test, launches 5 instances of the stress test process, useful for computers aging 7 to 13 years old with CPUs faster than 2 GHz
* 4 -> performs an even more advanced stress test, launches 15 instances of the stress test process, useful for computers aging 5 to 10 years old with CPUs faster than 2 GHz
* 5 -> performs an high end stress test, launches 35 instances of the stress test process, useful for computers aging 3 to 1 year old with CPUs faster than 3 GHz
* 6 -> performs a high end burnin stress test, launches 50 instances of the stress test process, useful for highend computers (really high end ones)
* 7 -> performs the best and highest burn in tests possible, launches 150 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION**
* 8 -> performs the INDESTRUCTABLE MONESTER STRESS TEST, launches 400 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION** **MIGHT BURN YOUR CPU**

To run a stress test, you have to **run a command prompt window as administrator**, then run `xcpustress.exe` using the following CLI syntax:
```bat
xcpustress/<Executable Filename>.exe [stress test mode]
```
* Where of course `[stress test mode]` must be replaced with the number of the stress test mode you want to run.

## CLI usage/syntax
```md
usage: xcpustress/<Executable Filename>(.exe/No extension) [stress test mode]
where:
* [stress test mode] can be any of the following:
1 -> performs a basic stress test, launches 1 instance of the stress test process, useful for very old computers with CPUs slower than 1 GHz
2 -> performs a more advanced stress test, launches 3 instances of the stress test process, useful for old computers with CPUs slower than 2 GHz
3 -> performs an even more advanced stress test, launches 5 instances of the stress test process, useful for computers aging 7 to 13 years old with CPUs faster than 2 GHz
4 -> performs an even more advanced stress test, launches 15 instances of the stress test process, useful for computers aging 5 to 10 years old with CPUs faster than 2 GHz
5 -> performs an high end stress test, launches 35 instances of the stress test process, useful for computers aging 3 to 1 year old with CPUs faster than 3 GHz
6 -> performs a high end burnin stress test, launches 50 instances of the stress test process, useful for highend computers (really high end ones)
7 -> performs the best and highest burn in tests possible, launches 150 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION**
8 -> performs the INDESTRUCTABLE MONESTER STRESS TEST, launches 400 instances of the stress test process, useful for monster PCs only! **USE WITH EXTREME CAUTION** **MIGHT BURN YOUR CPU**

examples:
xcpustress 1
* performs a basic stress test on the processor

xcpustress 2
* performs a level two stress test on the processor

xcpustress 3
* performs a level three stress test on the processor (somewhat good for 3rd generation i3/i5/i7 Intel CPUs or older)

xcpustress 4
* performs a level four stress test on the processor (It is recommended for most processors newer than 2012)

xcpustress 5
* performs a burnin stress test on the processor (mostly recommended for most processors, including older ones, can cause overheating, but *really* stresses the processor)


```

## Where to download?
Go to the [**Releases**](https://github.com/InsertX2k/xcpustress/releases) page in this repository, download the appropriate version according to your operating system.

## TODO

- [ ] Make a GUI wrapper for the app
- [ ] Compile a version for 32-bit windows versions.
- [ ] Compile a version for Linux
- [ ] Make the app display CPU usage percentages in both the console and the GUI versions.
- [ ] Improve this `README.md` file and include comparison screenshots between this stress test tool and other preparatory ones (**AIDA64, for example**).
- [ ] Improve the way this program handles **KeyboardInterrupts** (<kbd>Ctrl</kbd> + <kbd>C</kbd> Keyboard events)

## License
See `LICENSE`
