// See https://aka.ms/new-console-template for more information
using System.Diagnostics;

Console.WriteLine("Start!");
Benchmark(p1, 1000);

void p1()
{
    var factory = new FileAssigmentFactory("input.txt");

    int totalSubset = 0;
    int totalOverlap = 0;

    foreach ((var set1, var set2) in factory.GetAssigmentPairs())
    {
        bool hasSubset = set1.Count < set2.Count ? set1.IsSubsetOf(set2) : set2.IsSubsetOf(set1);
        bool overlap = set1.Overlaps(set2);
        if (hasSubset)
        {
            totalSubset++;
        }

        if (overlap)
        {
            totalOverlap++;
        }
    }
}

void Benchmark(Action act, int iterations)
{
    GC.Collect();
    act.Invoke(); // run once outside of loop to avoid initialization costs
    Stopwatch sw = Stopwatch.StartNew();
    for (int i = 0; i < iterations; i++)
    {
        act.Invoke();
    }
    sw.Stop();
    Console.WriteLine((sw.ElapsedMilliseconds * 1.0 / iterations).ToString());
}

class FileAssigmentFactory
{
    private string _file;
    public FileAssigmentFactory(string file)
    {
        _file = file;
    }

    public IEnumerable<Tuple<HashSet<int>, HashSet<int>>> GetAssigmentPairs()
    {
        foreach (var line in GetLines())
        {
            var sets = line.Split(',').Select(GetNumbers).ToArray();

            yield return new Tuple<HashSet<int>, HashSet<int>>(sets[0], sets[1]);
        }
    }

    private HashSet<int> GetNumbers(string range)
    {
        int[] numbers = range.Split('-').Select(s => int.Parse(s)).ToArray();
        return Enumerable.Range(numbers[0], numbers[1] - numbers[0] + 1).ToHashSet();
    }

    private IEnumerable<string> GetLines()
    {
        using (StreamReader reader = new StreamReader(_file))
        {
            string? line = null;
            while ((line = reader.ReadLine()) is not null)
            {
                yield return line;
            }
        }
    }
}