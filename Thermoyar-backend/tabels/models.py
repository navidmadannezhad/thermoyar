from django.db import models

class state(models.Model):
    state_name = models.CharField(max_length=10)

    def __str__(self):
        return self.state_name

class material(models.Model):
    material_name = models.CharField(max_length=10)

    def __str__(self):
        return self.material_name

class superheat(models.Model):
    state_n = models.ForeignKey(state, on_delete=models.CASCADE)
    material_n = models.ForeignKey(material, on_delete=models.CASCADE)
    temp = models.FloatField(max_length=5)
    pres = models.FloatField(max_length=5)
    vol = models.FloatField(max_length=8)
    eng = models.FloatField(max_length=8)
    antal = models.FloatField(max_length=8)
    ant = models.FloatField(max_length=8)

class sub_cold(models.Model):
    state_n = models.ForeignKey(state, on_delete=models.CASCADE)
    material_n = models.ForeignKey(material, on_delete=models.CASCADE)
    temp = models.FloatField(max_length=5)
    pres = models.FloatField(max_length=5)
    vol = models.FloatField(max_length=8)
    eng = models.FloatField(max_length=8)
    antal = models.FloatField(max_length=8)
    ant = models.FloatField(max_length=8)


class saturate(models.Model):
    state_n = models.ForeignKey(state, on_delete=models.CASCADE)
    material_n = models.ForeignKey(material, on_delete=models.CASCADE)
    temp = models.FloatField(max_length=5)
    pres = models.FloatField(max_length=5)
    vol_f = models.FloatField(max_length=8)
    vol_fg = models.FloatField(max_length=8)
    vol_g = models.FloatField(max_length=8)
    eng_f = models.FloatField(max_length=8)
    eng_fg = models.FloatField(max_length=8)
    eng_g = models.FloatField(max_length=8)
    antal_fe = models.FloatField(max_length=8)
    antal_fg = models.FloatField(max_length=8)
    antal_g = models.FloatField(max_length=8)
    ant_f = models.FloatField(max_length=8)
    ant_fg = models.FloatField(max_length=8)
    ant_g = models.FloatField(max_length=8)






