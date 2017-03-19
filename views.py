#tripSummaries is a list of date strings, start city string, end city string, and trip id (for button)
import datetime
import calendar

GAS_PRICE = 1.25
#Homepage header
#Trip ID // Start City // End City // Start Timestamp // Distance[m] // Fuel Efficiency[km/L]// Vehicle ID
def generateHomePage(tripSummaries):
    #WAY too many Altitudes to do right now...
    #pageAlt = 900
    #logoAlt = 900
    #repeaterAlt = 198
    #groupAlts = []

    startLocs = []
    endLocs = []
    dates = []

    #Find number of groups
    groupNum = len(tripSummaries)
    for n in range(0, groupNum):
        startLocs.append(tripSummaries[n][1]) #will need to change if using Dict input
        endLocs.append(tripSummaries[n][2])
        date = makeNiceDate(tripSummaries[n][3][0:10])

        dates.append(date)

    print(startLocs)
    print(endLocs)
    print(dates)

    HOMEHEAD = """<html>

<head>
<title> DIVID HOME </title>
</head>

<body>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 375 900">
  <defs>
    <style>
      .cls-1 {
        fill: none;
      }

      .cls-2 {
        clip-path: url(#clip-iPhone_6_7_1);
      }

      .cls-3 {
        fill: url(#pattern);
      }

      .cls-4, .cls-7 {
        fill: #95989a;
      }

      .cls-4 {
        font-size: 20px;
        font-family: OpenSans, Open Sans;
      }

      .cls-5 {
        clip-path: url(#clip-path);
      }

      .cls-6 {
        fill: #fff;
        stroke: #95989a;
      }

      .cls-7 {
        font-size: 16px;
        font-family: OpenSans-Bold, Open Sans;
        font-weight: 700;
      }

      .cls-8 {
        stroke: none;
      }

      .cls-9 {
        fill: #fcfff7;
      }
    </style>
    <pattern id="pattern" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" viewBox="0 0 416 292">
      <image width="416" height="292" xlink:href="data:image/png;base64,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"/>
    </pattern>
    <clipPath id="clip-path">
      <rect class="cls-1" width="330" height="137"/>
    </clipPath>
    <clipPath id="clip-iPhone_6_7_1">
      <rect width="375" height="900"/>
    </clipPath>
  </defs>
  <g id="iPhone_6_7_1" data-name="iPhone 6/7 – 1" class="cls-2">
    <rect class="cls-9" width="375" height="900"/>                                                                                                     <!-- page dimensions?  -->
    <rect id="DIVID_Alt_2" data-name="DIVID Alt 2" class="cls-3" width="123" height="86" transform="translate(126 22)"/>                                <!-- the logo at the top -->
    <text id="Choose_recent_trip:" data-name="Choose recent trip:" class="cls-4" transform="translate(23 155)"><tspan x="0" y="21">Choose recent trip:</tspan></text> <!-- "choose" text -->
    <g id="Repeat_Grid_1" data-name="Repeat Grid 1" class="cls-5" transform="translate(23 198)">                            <!-- this is the repeater grid, with specified location -->


  """

    ELEMENT = """
      <a href="{{URLToID}}">     <!-- CHANGE THIS to link to the second page! -->
        <g id="group" transform="translate(-28 {{NumberOffset}})">
            <g id="Rectangle_1" data-name="Rectangle 1" class="cls-6" transform="translate(28 240)">
                <rect class="cls-8" width="330" height="50" rx="25"/>
                <rect class="cls-1" x="0.5" y="0.5" width="329" height="49" rx="24.5"/>
            </g>                                                                                                                <!-- the text elements follow here -->
            <text id="{{StartLoc}}" class="cls-7" transform="translate(45 271)"><tspan x="0" y="0">{{StartLoc}}</tspan></text>        <!-- CHANGE THIS START LOCATION TEXT to match trip start -->
            <text id="{{DAAATE1}}" class="cls-7" transform="translate(252 254)"><tspan x="0" y="17">{{DAAATE1}}</tspan></text>           <!-- CHANGE THIS DATE TEXT to match trip date -->
            <text id="to" class="cls-7" transform="translate(136 254)"><tspan x="0" y="17">to</tspan></text>                        <!-- no need to change this -->
            <text id="EndLoc" data-name="{{EndLoc}}" class="cls-7" transform="translate(158 254)"><tspan x="0" y="17">{{EndLoc}} </tspan></text> <!-- CHANGE THIS END LOCATION TEXT to match trip -->
            </g>
      </a>

"""

    FOOTER = """

    </g>
  </g>
</svg>

</body>

</html>"""
    from jinja2 import Template

    t = Template(ELEMENT)
    i = 0;
    print(tripSummaries)
    for trip in tripSummaries:
        output = t.render(DAAATE1= makeNiceDate(trip[3][0:10]), StartLoc = trip[1], EndLoc = trip[2], NumberOffset = -240 + i * 70 )
        i = i + 1;

        HOMEHEAD = HOMEHEAD + output;


    print(HOMEHEAD + FOOTER);
    return (HOMEHEAD + FOOTER)

def makeNiceDate(date):
    date = str.replace(date, '-', '', 2)
    dateObj = datetime.datetime.strptime(date, '%Y%m%d').date()
    month = calendar.month_abbr[dateObj.month]
    day = str(dateObj.day)
    stringDate = month + ' ' + day
    return stringDate


#tripInfoList is a list of fuel-use floats, fuel-price floats, and trip id (for button)
def generateTripPage(tripSummaries):

    #Calculate fuel used
    efficiency = tripSummaries[5]
    distance = tripSummaries[4]/1000
    fuelConsumed = efficiency * distance / 100

    #Calculate cost of gas
    cost = fuelConsumed * GAS_PRICE
    # Find number of groups

    PAGE = """<html>

    <head>
    <title> My First Webpage </title>
    </head>

    <body>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="445 0 375 667">
      <defs>
        <style>
          .cls-1 {
            clip-path: url(#clip-iPhone_6_7_2);
          }

          .cls-2, .cls-5 {
            fill: #95989a;
          }

          .cls-2 {
            font-size: 24px;
          }

          .cls-2, .cls-4, .cls-5 {
            font-family: OpenSans, Open Sans;
          }

          .cls-3, .cls-4 {
            fill: #f15a24;
          }

          .cls-3 {
            font-size: 35px;
            font-family: OpenSans-Bold, Open Sans;
            font-weight: 700;
          }

          .cls-4 {
            font-size: 100px;
          }

          .cls-5 {
            font-size: 20px;
          }

          .cls-6 {
            fill: url(#pattern);
          }

          .cls-7 {
            fill: none;
          }

          .cls-7, .cls-8 {
            stroke: #c1272d;
            stroke-width: 3px;
          }

          .cls-8 {
            fill: rgba(0,0,0,0);
          }

          .cls-9 {
            fill: #fcfff7;
          }
        </style>
        <pattern id="pattern" preserveAspectRatio="xMidYMid slice" width="100%" height="100%" viewBox="0 0 416 292">
          <image width="416" height="292" xlink:href="data:image/png;base64,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"/>
        </pattern>
        <clipPath id="clip-iPhone_6_7_2">
          <rect x="445" width="375" height="667"/>  <!-- Viewport Dimensions (Currently optimized for mobile) -->
        </clipPath>
      </defs>


      <g id="iPhone_6_7_2" data-name="iPhone 6/7 – 2" class="cls-1">
        <rect class="cls-9" x="445" width="375" height="667"/>
        <text id="Fuel_used:_" data-name="Fuel used:" class="cls-2" transform="translate(498 67)"><tspan x="0" y="37">Fuel used:</tspan><tspan class="cls-3" y="37"></tspan></text> <!-- descriptor -->

        <text id="total_trip_cost_" data-name="total trip cost " class="cls-5" transform="translate(582 323)"><tspan x="28.742" y="21">total trip cost </tspan></text> <!-- descriptor -->
        <a href="http://www.google.com">                                                                                            <!-- CHANGE THIS to link to the Third page! -->
          <rect id="DIVID_Alt_2" data-name="DIVID Alt 2" class="cls-6" width="197" height="139" transform="translate(498 448)"/>              <!-- logo (no need to change) -->
        </a>
        <text id="_your_trip" data-name="…your trip" class="cls-5" transform="translate(596 553)"><tspan x="0" y="21">…your trip</tspan></text> <!-- descriptor -->
        <line id="Line_1" data-name="Line 1" class="cls-7" x2="90" y2="124" transform="translate(582.5 109.5)"/>
        <line id="Line_2" data-name="Line 2" class="cls-7" x1="83" y2="117" transform="translate(590.5 348.5)"/>
        <path id="Path_1" data-name="Path 1" class="cls-8" d="M0,0,22.305,82.855" transform="translate(590.5 587.5)"/>
        <line id="Line_4" data-name="Line 4" class="cls-7" y1="93" x2="45" transform="translate(582.5 -10.5)"/>
        <text id="_13.5L_" data-name="13.5L" class="cls-3" transform="translate(622 67)"><tspan x="0" y="37">{{consumption}} L</tspan></text>             <!-- CHANGE THIS TO MATCH FUEL CONSUMED -->
        <text id="_34" data-name="$34" class="cls-4" transform="translate(526 207)"><tspan x="61.233" y="107">${{fuelCost}}</tspan></text>          <!-- CHANGE THIS PRICE TO MATCH CALCULATED -->
      </g>


    </svg>

    </body>

    </html>"""

    from jinja2 import Template

    t = Template(PAGE)
    output = t.render(consumption=fuelConsumed, fuelCost=cost)

    print(output);
    return (output)


def generateRequestMoneyPage(tripIds):

    return 0

