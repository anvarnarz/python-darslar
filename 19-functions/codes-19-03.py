"""
16/12/2020

Dasturlash asoslari

#19-dars: FUNCTIONS (FUNKSIYALAR)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(
        f"Foydalanuvchi ismi: {ism.title()}\n"
        f"Foydalanuvchi familiyasi: {familiya.title()}"
    )


# toliq_ism('olim','hakimov')
# toliq_ism('hakimov','olim')


def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")


# yosh_hisobla('olim',1997)
# yosh_hisobla(1997,'olim')

# yosh_hisobla(ism='olim', t_yil=1997)
toliq_ism(familiya="hakimov", ism="olim")
