#tool to plan my IT projects
#counts ports needed for switches
#hopefully I get it to map to switch models/qty and add up power/heat


unet_seats = int(input("how many desks with UNET?"))

unet_cr_drops = int(input("how many active UNET drops in conference rooms?"))

unet_printers = int(input("how many UNET printers?"))

unet_VTC = int(input ("how many UNET VTCS?"))

unet_VOIP = int(input("how many UNET VOIP phones? incl STE or VIPEr"))

swsnet_servers = int(input("how many UNET ports are used by servers?")

unet_active_drops = unet_seats + unet_cr_drops + unet_printers + unet_VTC + unet_VOIP + unet_servers
unet_active_drops
unet_switchports_needed = unet_active_drops + 4
unet_PoE = input("are you using PoE for UNET")


s_seats = int(input("how many desks with SNET?"))

s_cr_drops = int(input("how many active SNET drops in conference rooms?"))

s_printers = int(input("how many SNET printers?"))

s_VTC = int(input ("how many SNET VTCS?"))

s_VOIP = int(input("how many SNET VOIP phones?"))
s_active_drops = s_seats + s_cr_drops + s_printers + s_VTC + s_VOIP
s_active_drops
s_switchports_needed = s_active_drops + 4
