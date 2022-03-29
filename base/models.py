from django.db import models


class UserTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    userAgency = models.CharField(max_length=100)
    userType_id = models.IntegerField()
    userDzongkhag = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class RegionDetails(models.Model):
    regionID = models.IntegerField(primary_key=True)
    regionName = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class Dzongkhag(models.Model):
    dzoID = models.IntegerField(primary_key=True)
    dzongkhagNames = models.CharField(max_length=100,)
    gewogs = models.CharField(max_length=100, null=True, blank=True)
    isRegion = models.BooleanField(default=False)
    createdDateTime = models.DateField(null=True,  blank=True)


class AgencyDetails(models.Model):
    agencyID = models.IntegerField(primary_key=True)
    agencyName = models.CharField(max_length=100)
    agencyLocation = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class EconomicDevelopmentType(models.Model):
    economicDevID = models.IntegerField(primary_key=True)
    economicDevType = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class IspDetails(models.Model):
    ispID = models.IntegerField(primary_key=True)
    ispName = models.CharField(max_length=100)
    ispLocation = models.CharField(max_length=100)
    isMobileOperators = models.BooleanField(default=False)


class BroadbandSubType(models.Model):
    broadbandID = models.IntegerField(primary_key=True)
    broadbandType = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class InternetServiceType(models.Model):
    ispID = models.IntegerField(primary_key=True)
    internetType = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class VehicleTypes(models.Model):
    LV = models.CharField(max_length=100)
    TW = models.CharField(max_length=100)


class InternetServiceData(models.Model):
    intDataID = models.IntegerField(primary_key=True)
    internetType = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    subscriber = models.CharField(max_length=100)
    populationUsingInternet = models.CharField(max_length=100)
    percentageIncrease = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=100)
    editedBy = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class BroadbandData(models.Model):
    bbDataID = models.IntegerField(primary_key=True)
    broadbandType = models.CharField(max_length=100)
    year = models.DateField(max_length=4)
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=100)
    editedBy = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class InternetType(models.Model):
    internetID = models.IntegerField(primary_key=True)
    internetType = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdBy = models.CharField(max_length=100)
    editedBy = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class MobileBroadbandType(models.Model):
    mobileBroadbandID = models.IntegerField(primary_key=True)
    mobileBroadbandType = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class PostalInfrastructure(models.Model):
    postalID = models.IntegerField(primary_key=True)
    postalInfrastructureType = models.CharField(max_length=100)
    postalServiceType = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class MediaHouse(models.Model):
    mediaID = models.IntegerField(primary_key=True)
    mediaHouseName = models.CharField(max_length=100)
    mediaHouseStarted = models.DateField()
    mediaHouseFrequencyPublication = models.IntegerField()
    year = models.DateField(max_length=4)
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class RadioBroadcasterData(models.Model):
    radioID = models.IntegerField(primary_key=True)
    radioBroadcasterName = models.CharField(max_length=100)
    radioBroadcasterStarted = models.DateField(max_length=4)
    radioBroadcasterCoverage = models.IntegerField()
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class Magazines(models.Model):
    magazineID = models.IntegerField(primary_key=True)
    magazineName = models.CharField(max_length=100)
    magazineStarted = models.DateField(max_length=4)
    magazineFrequencyPublication = models.IntegerField()
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class BookPublications(models.Model):
    bookPubID = models.IntegerField(primary_key=True)
    bookPubName = models.CharField(max_length=100)
    bookPubDzongkhag = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class FixedLineTelData(models.Model):
    tellID = models.IntegerField(primary_key=True)
    dzongkhagsConnected = models.CharField(max_length=100)
    telSubscriberNumber = models.CharField(max_length=100)
    percentageDiff = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class MobileData(models.Model):
    mobID = models.IntegerField(primary_key=True)
    dzongkhagsConnected = models.CharField(max_length=100)
    gewogsConnected = models.CharField(max_length=100)
    popuUsingMobile = models.CharField(max_length=100)
    mobSubscriberNumber = models.CharField(max_length=100)
    percentageDiff = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class TvStations(models.Model):
    tvID = models.IntegerField(primary_key=True)
    tvStationsName = models.CharField(max_length=100)
    tvStationsDzongkhag = models.CharField(max_length=100)
    tvStationsNumber = models.IntegerField()
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class CableOperators(models.Model):
    cableOperatorsID = models.IntegerField(primary_key=True)
    cableOperatorsName = models.CharField(max_length=100)
    cableOperatorsDzongkhag = models.CharField(max_length=100)
    cableOperatorsNumber = models.IntegerField()
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class PrintingPress(models.Model):
    printingPressID = models.IntegerField(primary_key=True)
    printingPressName = models.CharField(max_length=100)
    printingPressDzongkhag = models.CharField(max_length=100)
    printingPressNumber = models.IntegerField()
    printingPressTypes = models.IntegerField()
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class Aviation(models.Model):
    aviationID = models.IntegerField(primary_key=True)
    isPlane = models.BooleanField(default=False)
    isHelicopter = models.BooleanField(default=False)
    aviationName = models.CharField(max_length=100)
    aviationEstablished = models.DateField()
    operationRouteDomestic = models.CharField(max_length=1)
    operationRouteInternational = models.CharField(max_length=1)
    aircraftType = models.CharField(max_length=100)
    aircraftNumbers = models.CharField(max_length=100)
    helicopterType = models.CharField(max_length=100)
    seatingCapacity = models.IntegerField()
    year = models.DateField(max_length=4)
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class AirportType(models.Model):
    airportID = models.IntegerField(primary_key=True)
    airportRoute = models.CharField(max_length=100)
    airportDzongkhag = models.CharField(max_length=100)
    airportAltitude = models.CharField(max_length=100)
    airportRunwayLength = models.CharField(max_length=100)
    airportRunwayWidth = models.CharField(max_length=100)
    airportAerodromeRefCode = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class FlightDetails(models.Model):
    flightID = models.IntegerField(primary_key=True)
    flightRoute = models.CharField(max_length=100)
    flightLaunchDate = models.DateField()
    airportName = models.CharField(max_length=100)
    airportDzongkhag = models.CharField(max_length=100)
    airportAltitude = models.CharField(max_length=100)
    airportRunwayLength = models.CharField(max_length=100)
    airportRunwayWidth = models.CharField(max_length=100)
    airportAerodromeRefCode = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class FlightPurpose(models.Model):
    flightPurposeID = models.IntegerField(primary_key=True)
    flightPurposeRoute = models.CharField(max_length=100)
    flightLaunchDate = models.DateField()
    airportName = models.CharField(max_length=100)
    airportDzongkhag = models.CharField(max_length=100)
    airportAltitude = models.CharField(max_length=100)
    airportRunwayLength = models.CharField(max_length=100)
    airportRunwayWidth = models.CharField(max_length=100)
    airportAerodromeRefCode = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()


class SurfaceTransport(models.Model):
    transportID = models.IntegerField(primary_key=True)
    vehicleType = models.CharField(max_length=100)
    regionName = models.CharField(max_length=100)
    ownerType = models.CharField(max_length=100)
    year = models.DateField()
    quarter = models.IntegerField()
    remarks = models.CharField(max_length=100)
    createdDateTime = models.DateField()
