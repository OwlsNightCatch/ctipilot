---
title: "GitHub - mattifinder/rpmc_attacks: Artifacts for our paper \"Hello Again\", published at ACM CCS 2026"
url: https://github.com/mattifinder/rpmc_attacks
hostname: github.com
description: Artifacts for our paper "Hello Again", published at ACM CCS 2026 - mattifinder/rpmc_attacks
sitename: GitHub
date: "2024-11-04"
categories: ['repository:883382251']
fingerprint: "35d2521e0d238b6d"
language: en
image: https://opengraph.githubassets.com/7ba4bcec508d82d2d0ba4a2e0f7d9e780114589b28fff3e4d5b695cd84beb559/mattifinder/rpmc_attacks
pagetype: object
filedate: "2026-11-25"
---
This repository provides up-to-date information as well as supplemental material to our paper:
["Hello Again: Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs"](https://arxiv.org/abs/2611.18126) (originally published at ACM CCS 2026)

Important

tl;dr: If you rely on numeric Windows Hello or BitLocker PINs, **increase your PIN length by at least two digits**. Even in light of our attacks, this increases the time to bruteforce them from several days to months or even years.

In the paper, we introduce vulnerabilities in both RPMC flash chips (e.g., Winbond's) and RPMC controllers (e.g., AMD's). This repository is mainly a collection of code that helped us test for the respective vulnerabilities. It includes scripts to test a counter for integer overflows, conduct crowbar voltage glitching attacks to test for sensitive leakages, and firmware for an RP2350 allowing two types of interposition attacks: one exploiting AMD's unverified RPMC increments and another for forging RPMC replies when an attacker is in posession of an HMAC key (e.g., on a Winbond-based system vulnerable to voltage glitching). It also contains the hardware designs for our custom interposer PCB.

Note

With this repository, we try to make our code and data available for other researchers. Given the experimental nature of offensive hardware security research, reproduction of our attacks is not plug-and-play. Most importantly, it assumes access to our interposer PCB ([v1](https://github.com/mattifinder/rpmc_attacks/blob/main/interposer/v1) or [v2](https://github.com/mattifinder/rpmc_attacks/blob/main/interposer/v2)).

In our paper, we claim that the Lenovo IdeaPad 5 Pro 16ACH16 from 2021 does not use RPMC. Technically, this is correct, as the used flash chip (Winbond 74M series) does not support a technology called RPMC. However, as we found out only after the final deadline of the paper, **this flash series is already a so-called [Authentication Flash](https://www.winbond.com/productResource-files/Winbond_Authentication%20Flash_Product%20Brief.pdf) that is functionally identical and uses the exact same commands as the RPMC version.** We verified that it is used by tracing SPI flash during boot and our [Saleae RPMC analyzer](https://github.com/mattifinder/saleae-RPMC-analyzer) detected the commands right away. Most importantly, this falsifies our assumption that AMD prevents NV state rollbacks without RPMC (or *Authentication Flash*) on that system.

Secondly, we re-tested naive NV state rollbacks on additional systems, both by AMD and Intel, to better understand if pre-RPMC NV rollabck protection existed:

- Two AMD-based systems without access to RPMC(-like) SPI flash (Winbond W25Q series)
  - A Zen 2-based ASUS desktop mainboard
  - A Zen 5-based MSI PRO desktop mainboard
- Two Intel-based systems without access to RPMC(-like) SPI flash
  - An Intel Core i3-4170 on an ASUS H81M-PLUS
  - An Intel Core i5-14400 on an MSI PRO B760M-P DDR4

**While the Intel sytems defended against the naive rollbacks, both AMD systems did not. They allowed us to reliably reset the TPM's dictionary attack counters only by reprogramming an old NV state onto the SPI flash using an SPI programmer; no interposer required.**

While these two observations may not be representative of all AMD systems, our key insights are these:

1. **RPMC was already used on systems as early as 2021**, despite being called *[Authentication Flash](https://www.winbond.com/productResource-files/Winbond_Authentication%20Flash_Product%20Brief.pdf)* by Winbond.
2. A Zen 2-based desktop **system without access to RPMC-like SPI flash allows naive rollbacks** of the NV state.
3. Our assumption that **AMD SoCs feature standalone rollback protection for their NV state** was **probably wrong**.
(Our highlighted recommendation to fix the current issues with both RPMC controllers and flash  by falling back to those (Section 6 - "RPMC Security") is, therefore, worthless.)

Intel in contrast does seem to have their own pre-RPMC rollback protection, since we couldn't naively rollback the NV state on the Acer Aspire, whose Macronix MX25U25672G doesn't have a comparable feature.

A simple optimization of our KVM's attack loop sped up the overall duration of the 236-try brute-force campaign from 8min 40s to 6min 55s, so by \~ 20%. This decreases the worst-case **brute-force times for a default-length 6-digit BitLocker PIN from 26 days to \~ 20 days**.

As of now, two sorts of systems are affected by our end-to-end attacks enabling fTPM rollback (and therefore dysfunctional anti-hammering/brute-force protection):

1. **AMD-based** systems (any flash vendor, with or without RPMC; RPMC-based protection may be fixed by future AMD firmware updates)
2. Systems relying on **Winbond RPMC flash** for its x86 firmware (UEFI/BIOS)

On Windows, press `Win + I`, go to System -> About. Under "Device specifications", the Processor line shows the exact model.

On Linux, open up a Terminal and run `lscpu`.

If your system uses an AMD CPU, it is prone to either naive NV state rollbacks (using only an SPI Flash programmer) or, if it relies on RPMC to protect against NV state rollbacks, against attacks from our interposer suppressing the RPMC counter increments.

Unlike on Intel, AMD systems can tell from software whether RPMC is in use. Since Linux 5.19, the `ccp` driver exports the PSP's security attributes via sysfs ([documentation](https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-driver-ccp)), including:

- `rpmc_spirom_available`: whether an RPMC-capable SPI flash is present
- `rpmc_production_enabled`: whether RPMC has been enabled

On Linux (e.g., booted from a live USB stick), run:

`grep . /sys/bus/pci/drivers/ccp/*/rpmc_*`
Alternatively, the firmware update daemon [fwupd](https://fwupd.github.io/libfwupdplugin/hsi.html) summarizes both attributes in its *AMD SPI Replay protections* attribute, displayed by:

`fwupdmgr security`
These reports match our results: The Lenovo IdeaPad 5 Pro 16ACH16, whose Authentication Flash supports RPMC commands, reports both attributes as `1` and detected naive rollbacks, whereas the Zen 2 desktop reports both as `0` and accepted them.

Note

The PSP exports these attributes only on select SoCs. If the files are missing (or fwupd cannot report the attribute), this does **not** imply that your system lacks RPMC.

Either way, an AMD system is exposed to one of the two rollback paths: the *Unverified Increment* attack via an interposer if RPMC is used, or a naive rollback via an SPI programmer if it is not.

For Intel systems, we are not aware of an interface comparable to AMD's (see above). Whether they rely on RPMC can, to our knowledge, only be identified through inspection of the mainboard and SPI bus traffic. Unfortunately, telling the SPI flash manufacturer from running OS is impossible on a lot of systems. Moreso, OEMs may source SPI flash from multiple vendors for a single model.

Open up the back of your laptop and look for a black rectangular chip with markings like Winbond, Macronix, GigaDevice. Winbond's RPMC-capable series are labelled 74M or 25R and it is very likely that those are specifically there to enable the rollback protection of NV state on both Intel and AMD.

Lastly, to be sure that RPMC is used during boot, we recommend recording a logic analyzer trace of the SPI bus during boot (single SPI suffices as RPMC does not use Dual or Quad SPI). Our [RPMC analyzer for Saleae Logic](https://github.com/mattifinder/saleae-RPMC-analyzer) can help identify RPMC traffic. Counter retrievals and increments during boot will most likely come from RPMC-backed NV state rollback protection.

- `pocs` contains the Python scripts we used to test the flash chips in isolation
- `kvm_scripts` contains the scripts we used for our nano kvm to film the demo video and test the full end-to-end pin brute force
- `src` contains the firmware code for the interposer's RP2350 that makes heavy use of PIO state machines; see "Building" below
- `interposer` contains the kicad projects for the two versions of the interposer PCB
- `traces` contains some additional traces, more information in section "Traces & Supplemental Videos"
- `videos` contains two recordings of our E2E attacks which are also on YouTube: [`amd_hello.mp4`](https://www.youtube.com/watch?v=Yq2Wa-nj68g), [`wintel_bitlocker.mp4`](https://www.youtube.com/watch?v=MnplktYLMJw)

The projects are tested on the **Raspberry Pi Pico 2 (W)** sitting on one of our two custom interposer PCBs.

Build all subprojects with:

```
# arm-none-eabi toolchain with libc required
export PICO_TOOLCHAIN_PATH=/somewhere/on/your/filesystem/arm-none-eabi-gcc/16.2.0/bin
# https://github.com/raspberrypi/pico-sdk
export PICO_SDK_PATH=/somewhere/on/your/filesystem/pico-sdk
mkdir build
cd build
cmake ..
make -j
```
Deploy a specific project to the USB-attached Pico with:

`picotool load -f <subproject>.elf`
This project is used to increment a counter to a value of *UINT32\_MAX* hopefully allowing for an overflow back to 0.
Alternatively `pocs/counter_overflow.py` can be used as well.

This project allows for quicker voltage glitching iteration by receiving the delay used in the voltage glitch via serial.
It is meant to be used in conjunction with some of the scripts found in the `pocs` directory.

*Glitch\_finder* is very similar to *serprog\_glitch* but useful for quickly iterating through different values for the MOSFET open delay for testing and parameter finding.

Our values for the delay functions should only be used as a reference. Even for us the parameters always seem to change slightly when reusing the setup a couple months later. To reliably find the parameters, we recommend using a logic analyzer to observe the PIN controlling the MOSFET, the voltage rail, and the SPI transmission lines and then trying values that come close to the absolute times specified in the paper.

The lines in the source code that most likely will need to be adjusted are found in `src/serprog_with_glitch.c` and `pocs/voltage_glitching.py`.
Just look for *glitch\_cycles* or *delay*.

If that doesn't work, the next option is iterating through the whole search space to find values where the target starts to behave weirdly. Once found iterations on the setup should be performed, to e.g. reduce the resistance on the crowbar circuit. This is especially necessary if attempting to glitch a chip still soldered onto a laptop mainboard.

Interposer used to mount the attacks against our target systems.
To set the specific mode you have to open a tty to the pico (`picocom -b 115200 -q /dev/<your tty>`) and then enter the corresponding letter:

- a for AMD interposing (only v1)
- i for Intel interposing (only v2)
- r for writing an old spi state
- other for just passing traffic through to the chip

For automating our attack path, we included logic to rollback the necessary flash sections.
Rollbacking the whole flash is also possible, but inefficient, though this is a good first test to see if everything works.
To find them we looked for the sections that changed and extracted them using [psptool](https://github.com/pspreverse/psptool) and then converting them to header format using `xxd -i`.
In our case these were the sections *PSP\_NVRAM* (0x1100000 size 0x40000), *PSP\_NV\_DATA* (0x10e0000 size 0x20000), and *ROM\_ARMOR\_BIOS\_NVSTORE* (x1060000 size 0x40000).
Because these large files fill up the picos storage, we needed to perform some optimization on one of them to remove trailing 0xff and then implement the clearing of these bytes in another loop (see `reprogram_flash()`).
All these values need to be put in the `include/psp_nvdata.h` file.

This applies very similarly to Intel and the `include/intel_flash_rollback.h` file.

Because of signal integrity issues when using our interposer, we sadly couldn't perform the attacks while the laptops were using the full 80-100 MHz Quad SPI bandwidth available with these chips. Luckily, we found ways on both Intel and AMD to lower the SPI bus speed. While on Intel, this configuration is not cryptographically protected at all, AMD systems required replaying an AMD-signed configuration block from another system.

We found that the SPI clock speed of certain SPI transactions can be lowered by changing the *SpiRomConfig* blob (part of the PSP firmware blobs).
While this configuration is signed by AMD, we found versions of it in the public coreboot project that are signed by the same key that our target's firmware expects ([https://github.com/coreboot/amd\_blobs/tree/main/mendocino/PSP](https://github.com/coreboot/amd_blobs/tree/main/mendocino/PSP)).
More so, they contain versions of this config that are named after the SPI transmission method (Normal/Dual SPI) and frequency (16, 33, 66).
By replacing the existing *SpiRomConfig* blob with the *TypeId0x5C\_SpiRomConfig\_MDN\_Normal16.sbin* version from coreboot, we successfully lowered the SPI transaction speed.
While this noticeably increases boot time, it enabled our interposition using the low-cost hardware introduced in the paper.

At the time of writing, the [coreboot project](https://github.com/coreboot/coreboot) provides a utility program called *ifdtool* that can modify the Intel firmware descriptor.
The tool can be found in `util/ifdtool` and built using the provided Makefile.
To use this tool one needs to first extract a valid flash image and then subsequently write it back.
This tool provides an option to also set the SPI speed to a desired value; in our case, we choose the lowest available one.

```
ifdtool -s 17 -p <platform> -O <outimage> <inimage>
```
The traces were captured using a Saleae Logic Pro 16 and can be viewed using [Logic2](https://www.saleae.com/downloads).
They show for both AMD and Intel, one boot and also the behaviour when entering a wrong PIN i.e. an fTPM state change.

Proof of concept videos can be found on YouTube.
For [AMD](https://youtu.be/Yq2Wa-nj68g) we brute-forced Windows Hello pins and for [Intel](https://youtu.be/MnplktYLMJw) we targetted the Bitlocker + PIN entry.
