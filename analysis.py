import matplotlib.pyplot as plt
from data_ingestion import load_data, aggregate_by_day

def plot(daily_data):
    plt.figure(figsize=(10, 5))
    plt.plot(daily_data.index, daily_data['price'], marker='o', linestyle='-')
    plt.title('Total Price by Day')
    plt.xlabel('Day Index')
    plt.ylabel('Total Price')
    plt.grid(True)
    plt.savefig("TotalPriceByDay.jpg")
    plt.show()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Day Index')
    ax1.set_ylabel('Total Transactions', color=color)
    ax1.plot(daily_data.index, daily_data['customer_id'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Total Views', color=color)
    ax2.plot(daily_data.index, daily_data['times_viewed'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Total Transactions and Views by Day')
    plt.savefig("TotalTransactionsAndViewsByDay.jpg")

    plt.show()


if __name__ == "__main__":
    # Example
    file_paths = ['Data/cs-train/invoices-2017-11.json', 'Data/cs-train/invoices-2017-12.json'
                  ,'Data/cs-train/invoices-2018-01.json','Data/cs-train/invoices-2018-02.json']

    data = load_data(file_paths)
    daily_data = aggregate_by_day(data)

    plot(daily_data)
