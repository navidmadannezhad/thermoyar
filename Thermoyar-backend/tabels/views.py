from .models import superheat, sub_cold, saturate
from .serializers import superheatserializer, sub_coldserializer, saturateserializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .finder import finder
from .validator import validator
from rest_framework.decorators import api_view


class SuperHeatList(APIView):
	def post(self, request):
		whatIsWanted = request.data['wanted']
		givenPressure = request.data['pressure']
		givenTemperature = request.data['temperature']
		material = request.data['material']

		if validator.anyInputIsEmpty(whatIsWanted, givenPressure, givenTemperature):
			return Response('مقادیر رو کامل پر کن!')

		if validator.inputHasLetter(givenTemperature):
			return Response('ورودی غیر مجاز!')

		givenTemperature = float(givenTemperature)
		allRecords = superheat.objects.filter(material_n_id = material)
		allTemps = []

		for record in allRecords:
			allTemps.append(record.temp)
		allTemps = sorted(allTemps)

		try:
			wantedObject = allRecords.get(temp = givenTemperature, pres=givenPressure)
			wantedData = getattr(wantedObject, whatIsWanted)
			roundedWantedData = round(wantedData, 3)
			return Response(roundedWantedData)
		except:
			try:
				prevTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[0]
				nextTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[1]
			except:
				return Response('دمای مورد نظر خارج از جدول فوق داغه')

			try:
				prevObject = superheat.objects.filter(pres = givenPressure, material_n_id=material).get(temp = prevTemperature)
				prevParameter = getattr(prevObject, whatIsWanted)
				nextObject = superheat.objects.filter(pres = givenPressure, material_n_id=material).get(temp = nextTemperature)
				nextParameter = getattr(nextObject, whatIsWanted)
			except:
				return Response('دمای مورد نظر تحت این فشار فوق داغ نیست')

			wantedData = finder.interpolate(prevTemperature, prevParameter, givenTemperature, nextTemperature, nextParameter)

			roundedWantedData = round(wantedData, 4)
			return Response(roundedWantedData)



class Sub_ColdList(APIView):
	def post(self, request):
		whatIsWanted = request.data['wanted']
		givenPressure = request.data['pressure']
		givenTemperature = request.data['temperature']
		material = request.data['material']

		if validator.anyInputIsEmpty(whatIsWanted, givenPressure, givenTemperature):
			return Response('مقادیر رو کامل پر کن!')
		
		if validator.inputHasLetter(givenTemperature):
			return Response('ورودی غیر مجاز!')

		givenTemperature = float(givenTemperature)
		allRecords = sub_cold.objects.filter(material_n_id = material)
		allTemps = []

		for record in allRecords:
			allTemps.append(record.temp)
		allTemps = sorted(allTemps)

		try:
			wantedObject = allRecords.get(temp = givenTemperature, pres=givenPressure)
			wantedData = getattr(wantedObject, whatIsWanted)
			roundedWantedData = round(wantedData, 3)
			return Response(roundedWantedData)
		except:
			try:
				prevTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[0]
				nextTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[1]
			except:
				return Response('دمای مورد نظر خارج از جدول مادون سرده!')

			try:
				prevObject = sub_cold.objects.filter(pres = givenPressure, material_n_id=material).get(temp = prevTemperature)
				prevParameter = getattr(prevObject, whatIsWanted)
				nextObject = sub_cold.objects.filter(pres = givenPressure, material_n_id=material).get(temp = nextTemperature)
				nextParameter = getattr(nextObject, whatIsWanted)
			except:
				return Response('دمای مورد نظر تحت این فشار مادون سرد نیست')

			wantedData = finder.interpolate(prevTemperature, prevParameter, givenTemperature, nextTemperature, nextParameter)

			roundedWantedData = round(wantedData, 4)
			return Response(roundedWantedData)



class saturateList(APIView):
	def post(self, request):
		whatIsWanted = request.data['wanted']
		givenPressure = request.data['pressure']
		givenTemperature = request.data['temperature']
		material = request.data['material']

		if validator.anyInputIsEmpty(whatIsWanted):
			return Response('مقادیر رو کامل پر کن!')

		if validator.anyInputIsEmpty(givenTemperature) and validator.anyInputIsEmpty(givenPressure):
			return Response('مقادیر رو کامل پر کن!')

		allRecords = saturate.objects.filter(material_n_id = material)
		allTemps = []
		allPres = []

		for record in allRecords:
			allTemps.append(record.temp)
			allPres.append(record.pres)

		if givenPressure and givenTemperature:
			return Response('هم دما و هم فشار رو وارد نکن. فقط یکی!')


		if givenTemperature:
			if validator.inputHasLetter(givenTemperature):
				return Response('ورودی غیر مجاز!')
			givenTemperature = float(givenTemperature)
			try:
				wantedObject = allRecords.get(temp = givenTemperature)
				wantedData = getattr(wantedObject, whatIsWanted)
				roundedWantedData = round(wantedData, 3)
				return Response(roundedWantedData)
			except:
				try:
					prevTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[0]
					nextTemperature = finder.find_nearest_values(target_list = allTemps, target_value = givenTemperature)[1]
				except:
					return Response('داده مورد نظر تو جدول اشباع نیست')

				prevObject = saturate.objects.get(temp = prevTemperature, material_n_id=material)
				prevParameter = getattr(prevObject, whatIsWanted)
				nextObject = saturate.objects.get(temp = nextTemperature, material_n_id=material)
				nextParameter = getattr(nextObject, whatIsWanted)

				wantedData = finder.interpolate(prevTemperature, prevParameter, givenTemperature, nextTemperature, nextParameter)

				roundedWantedData = round(wantedData, 3)
				return Response(roundedWantedData)


		elif givenPressure:
			if validator.inputHasLetter(givenPressure):
				return Response('ورودی غیر مجاز!')
			givenPressure = float(givenPressure)
			try:
				wantedObject = allRecords.get(pres = givenPressure)
				wantedData = getattr(wantedObject, whatIsWanted)
				roundedWantedData = round(wantedData, 3)
				return Response(roundedWantedData)
			except:
				try:
					prevPressure = finder.find_nearest_values(target_list = allPres, target_value = givenPressure)[0]
					nextPressure = finder.find_nearest_values(target_list = allPres, target_value = givenPressure)[1]
				except:
					return Response('داده مورد نظر تو جدول اشباع نیست')

				prevObject = saturate.objects.get(pres = prevPressure, material_n_id=material)
				prevParameter = getattr(prevObject, whatIsWanted)
				nextObject = saturate.objects.get(pres = nextPressure, material_n_id=material)
				nextParameter = getattr(nextObject, whatIsWanted)

				wantedData = finder.interpolate(prevPressure, prevParameter, givenPressure, nextPressure, nextParameter)

				roundedWantedData = round(wantedData, 3)
				return Response(roundedWantedData)