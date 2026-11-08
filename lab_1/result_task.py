import sys


def main():
    # python lab_1/result_task.py lab_1/text.txt
    city_stats = {}
    try:
        with open(sys.argv[1]) as f:
            for line in f:
                data = line.strip()
                data = data.split(";")
                city = data[0]
                temperature = float(data[1])
                if city not in city_stats:
                    city_stats[city] = [temperature, temperature, temperature, 1]
                else:
                    city_stats[city][0] = min(city_stats[city][0], temperature)
                    city_stats[city][1] = max(city_stats[city][1], temperature)
                    city_stats[city][3] += 1
                    city_stats[city][2] += temperature
        for key in sorted(city_stats):
            average_city_value = city_stats[key][2] / city_stats[key][3]

            print(
                f"{key};{city_stats[key][0]};{average_city_value:.1f};{ city_stats[key][1]}"
            )
    except :
        print("ERROR")
  
if __name__ == "__main__":
    main()
