# agile-team

Baş Mimar'ın özel danışma kurulu: HLD, LLD, ADR ve yerel draw.io çizimleri. Ortam: Spring Boot ve OpenShift üzerinde Kafka.

Plan çizimi: [docs/architecture/ekip-plani.drawio](docs/architecture/ekip-plani.drawio)

## Ekip
Bu ekip kod yazmaz. Baş Mimar'ın danışma kuruludur: neyi, nasıl ve ne ile yapacağımızı netleştirir, HLD, LLD, ADR ve çizimleri üretir.

| Rol | Ajan | İş |
|---|---|---|
| Baş Mimar | `solution-architect` | Lider, HLD, ADR, üst düzey çizimler |
| Solution Designer | `solution-designer` | LLD, ayrıntılı çizimler |
| Java Uzmanı | `java-expert` | Uygulanabilirlik, teknoloji, çaba |
| Kafka Uzmanı | `kafka-expert` | Olay tasarımı, Kafka ayarları |
| Test Uzmanı | `test-expert` | Test edilebilirlik, ölçülebilirlik |
| OpenShift Uzmanı | `openshift-expert` | Dağıtım, kapasite, işletim |

## Kurulum
```bash
claude plugin marketplace add ~/Desktop/projects/agile-team
claude plugin install agile-team@agile-team-local
```

Bir değişiklikten sonra `plugin.json` ve `marketplace.json` içindeki sürümü artır, ardından:

```bash
claude plugin marketplace update agile-team-local
claude plugin update agile-team@agile-team-local
```

## Kullanım
Çalışma klasöründe `/agile-team:mimar <konu>` yaz. Çıktılar `docs/architecture/` altına yazılır.

## Gizlilik
Depo özeldir. Çizimler yalnızca yerel `.drawio` dosyası olarak üretilir, uzak bir servise gönderilmez. Şirkete ait kod, müşteri verisi ve gizli anahtar bu depoya konmaz.

## Lisans
Kişisel kullanım içindir. `skills/drawio/SKILL.md` jgraph/drawio-mcp projesinden alınmıştır (Apache-2.0), bkz. `skills/drawio/NOTICE`.
